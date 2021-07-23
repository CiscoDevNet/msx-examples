#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#

import uuid
import logging
import psycopg2

from config import Config
from config import CockroachConfig

from helpers.consul_helper import ConsulHelper
from helpers.vault_helper import VaultHelper


new_language_dict =  {  'id' :          '55f3028f-1b94-4edd-b14f-183b51b33d68',
                        'name':         'Russian',
                        'description':  'An East Slavic language that uses the Cyrillic alphabet.' }

new_item_dict = {   'id':          '62ef8e5f-628a-4f8b-92c9-485981205d92',
                    'languageid':  '55f3028f-1b94-4edd-b14f-183b51b33d68',
                    'languagename':'Russian',
                    'value' :       'Привет мир!' }


class CockroachHelper(object):
    def __init__(self, config: Config):

        consul_helper = ConsulHelper(config.consul)
        vault_helper = VaultHelper(config.vault)
        cockroach_config = config.cockroach

        self._conn = None
        self._databasename  = consul_helper.get_string("thirdpartyservices/defaultapplication/db.cockroach.databaseName",   cockroach_config.databasename )
        self._host          = consul_helper.get_string("thirdpartyservices/defaultapplication/db.cockroach.host",           cockroach_config.host )
        self._port          = consul_helper.get_string("thirdpartyservices/defaultapplication/db.cockroach.port",           cockroach_config.port )
        self._username      = consul_helper.get_string("thirdpartyservices/helloworldservice/db.cockroach.username",        cockroach_config.username )
        self._sslmode       = consul_helper.get_string("thirdpartyservices/helloworldservice/db.cockroach.sslmode",         cockroach_config.sslmode )
        self._password      = vault_helper.get_string("secret/thirdpartyservices/helloworldservice",  "db.cockroach.password",  "" )
        self._cacert        = cockroach_config.cacert


    def __enter__(self):
        if self._sslmode == 'disable':
            connection_str = f'postgres://{self._username}:{self._password}@{self._host}:{self._port}/{self._databasename}?sslmode={self._sslmode}'
            # connection_str = f'dbname={self._databasename} host={self._host} port={self._port} user={self._username} sslmode={self._sslmode}'
        else:
            connection_str = f'postgres://{self._username}:{self._password}@{self._host}:{self._port}/{self._databasename}?sslmode={self._sslmode}&sslrootcert={self._cacert}'
            # connection_str = f'dbname={self._databasename} host={self._host} port={self._port} user={self._username} password={self._password} sslmode={self._sslmode} sslrootcert={self._cacert}'
       
        logging.info(f'Connecting {connection_str}')
        self._conn = psycopg2.connect(connection_str)
        logging.info(f'Connetion status={self._conn.status}')
        return self


    def __exit__(self, ex_type, ex_value, traceback):
        logging.info('Closing db connection ...')
        self._conn.close()
        logging.info('Db connection closed')

        if ex_type:
            logging.info(f'{ex_type}{ex_value}{traceback}')

        return False   # return True if you want to supress full excption msg and stack trace


    def log_status(self):
        logging.info(f'Connetion status={self._conn.status}')


    def log_column(self, table, column):
        rows = self.get_rows(table)
        res = [row[column] for row  in rows]
        logging.info(f'{column}@{table}= {str(res)}')


    def test(self):        
        print(self.create_table('Languages', ['id', 'name', 'description']))
        print(self.create_table('Items', ['id', 'languageid', 'languagename', 'value']))

        self.log_column('Languages', 'name')
        self.log_column('Items','languagename')
   
        print(self.insert_row('Languages', new_language_dict))
        print(self.insert_row('Items', new_item_dict))

        self.log_column('Languages', 'name')
        self.log_column('Items','languagename')

        self.log_column('Items','value')
        print(self.update_row('Items', '62ef8e5f-628a-4f8b-92c9-485981205d92',  'value', 'Привет рим!'))
        self.log_column('Items','value')

        print(self.delete_row('Languages', '55f3028f-1b94-4edd-b14f-183b51b33d68'))
        print(self.delete_row('Items', '62ef8e5f-628a-4f8b-92c9-485981205d92'))

        self.log_column('Languages', 'name')
        self.log_column('Items','languagename')


    def get_rows(self, table_name):
        listof_rows = []
        query = f'SELECT * FROM {table_name}'

        logging.info(f'Exceuting={query}')
        with self._conn.cursor() as cur:
            cur.execute(query)
            # logging.info(f'execute: status message={cur.statusmessage}')
            columns = [desc[0] for desc in cur.description]
            rows = cur.fetchall()
            self._conn.commit()
            for row in rows:
                row_dict = dict(zip(columns,row))
                listof_rows.append(row_dict)
            statusmessage = cur.statusmessage
        
        logging.info(f'statusmessage={statusmessage}')
        return listof_rows


    def get_row(self, tablename, keyvalue):
        listof_rows = []
        query = f"SELECT * FROM {tablename}  where ID='{keyvalue}'"

        logging.info('Exceuting={query}')
        with self._conn.cursor() as cur:
            cur.execute(query)
            logging.info(f'Cursor execute: status message={cur.statusmessage}')
            columns = [desc[0] for desc in cur.description]
            row = cur.fetchone()
            self._conn.commit()
            row_dict = dict(zip(columns,row))
            listof_rows.append(row_dict)
            statusmessage = cur.statusmessage
        
        logging.info(f'statusmessage={statusmessage}')
        return listof_rows


    def update_row(self, tablename, id, coulmnname, columnvalue):
        update_clause = f"UPDATE {tablename} SET {coulmnname} = '{columnvalue}' WHERE id = '{id}'"

        logging.info(f'Exceuting={update_clause}')
        with self._conn.cursor() as cur:
            cur.execute(update_clause)
            statusmessage = cur.statusmessage

        self._conn.commit()
        logging.info(f'statusmessage={statusmessage}')
        return statusmessage


    def create_table(self, tablename, col_name_list):
        columns = '  STRING, '.join(col_name_list) + '  STRING' + ', PRIMARY KEY (' + col_name_list[0] + ')'                             
        create_clause = f'CREATE TABLE IF NOT EXISTS {tablename} ({columns})'

        logging.info(f'Exceuting={create_clause}')
        with self._conn.cursor() as cur:
            cur.execute(create_clause)
            statusmessage = cur.statusmessage

        self._conn.commit()
        logging.info(f'statusmessage={statusmessage}')
        return statusmessage


    def insert_row(self, tablename, row_values_dict):
        row_values_dict['id'] = str(uuid.uuid4())
        columns = ','.join(row_values_dict.keys())
        values = ','.join(  "'" + key + "'"  for key in  row_values_dict.values() )
        upsert_clause = f'UPSERT INTO {tablename} ({columns}) VALUES ({values})'

        logging.info('Exceuting='+upsert_clause)
        with self._conn.cursor() as cur:
            cur.execute(upsert_clause)
            statusmessage = cur.statusmessage

        self._conn.commit()
        logging.info(f'statusmessage={statusmessage}')
        return statusmessage


    def delete_row(self, tablename, id):
        delete_clause = f"DELETE FROM {tablename} WHERE ID='{id}'"

        logging.info('Exceuting='+delete_clause)
        with self._conn.cursor() as cur:
            cur.execute(delete_clause)
            statusmessage = cur.statusmessage

        self._conn.commit()
        logging.info(f'statusmessage={statusmessage}')
        return statusmessage


    def delete_rows(self, tablename):
        delete_clause = f"DELETE FROM {tablename}"

        logging.info('Exceuting='+delete_clause)
        with self._conn.cursor() as cur:
            cur.execute(delete_clause)
            statusmessage = cur.statusmessage

        self._conn.commit()
        logging.info(f'statusmessage={statusmessage}')
        return statusmessage
   

def main():
    config = Config("helloworld.yml")

    with CockroachHelper(config.cockroach) as db:
        db.log_status()
        db.test()

if __name__ == "__main__":
    main()
