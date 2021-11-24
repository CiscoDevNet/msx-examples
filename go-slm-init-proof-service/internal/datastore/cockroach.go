//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package datastore

import (
	"context"
	"fmt"
	"log"

	openapi "github.com/CiscoDevNet/msx-examples/go-slm-init-proof-service/go"
	"github.com/CiscoDevNet/msx-examples/go-slm-init-proof-service/internal/config"
	"github.com/CiscoDevNet/msx-examples/go-slm-init-proof-service/internal/consul"
	"github.com/CiscoDevNet/msx-examples/go-slm-init-proof-service/internal/vault"
	"github.com/google/uuid"
	"github.com/jackc/pgx/v4"
	"github.com/jackc/pgx/v4/pgxpool"
)

var schema = `
CREATE TABLE IF NOT EXISTS helloworld.ITEMS(
ID STRING,
LanguageId STRING,
LanguageName STRING,
Value STRING,
PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS helloworld.LANGUAGES(
ID STRING,
Name STRING,
Description STRING,
PRIMARY KEY (ID)
);
`

// Cockroach is a representation of a CockroachDB Database.
type Cockroach struct {
	Pool *pgxpool.Pool
}

func UpdateConfig(c *config.Config, consul *consul.HelloWorldConsul, vault *vault.HelloWorldVault) error {
	c.Cockroach.Host, _ = consul.GetString(c.Consul.Prefix+"/defaultapplication/db.cockroach.host", c.Cockroach.Host)
	c.Cockroach.Port, _ = consul.GetString(c.Consul.Prefix+"/defaultapplication/db.cockroach.port", c.Cockroach.Port)
	c.Cockroach.SSLMode, _ = consul.GetString(c.Consul.Prefix+"/defaultapplication/db.cockroach.sslmode", c.Cockroach.SSLMode)
	c.Cockroach.DatabaseName, _ = consul.GetString(c.Consul.Prefix+"/helloworldservice/db.cockroach.databaseName", c.Cockroach.DatabaseName)
	c.Cockroach.Username, _ = consul.GetString(c.Consul.Prefix+"/helloworldservice/db.cockroach.username", c.Cockroach.Username)
	c.Cockroach.Password, _ = vault.GetString(c.Vault.Prefix+"/helloworldservice", "db.cockroach.password", c.Cockroach.Password)
	return nil
}

func NewCockroachDB(c *config.Config) (*Cockroach, error) {
	connString := ""
	if c.Cockroach.SSLMode == "disable" {
		connString = fmt.Sprintf("postgres://%s@%s:%s/%s?sslmode=%s",
			c.Cockroach.Username,
			c.Cockroach.Host,
			c.Cockroach.Port,
			c.Cockroach.DatabaseName,
			c.Cockroach.SSLMode)
	} else {
		connString = fmt.Sprintf("postgres://%s:%s@%s:%s/%s?sslmode=%s&sslrootcert=%s",
			c.Cockroach.Username,
			c.Cockroach.Password,
			c.Cockroach.Host,
			c.Cockroach.Port,
			c.Cockroach.DatabaseName,
			c.Cockroach.SSLMode,
			c.Cockroach.CACert)
	}

	conf, err := pgxpool.ParseConfig(connString)
	if err != nil {
		return nil, err
	}
	p, err := pgxpool.ConnectConfig(context.Background(), conf)
	return &Cockroach{p}, err
}

func (c Cockroach) BuildSchema() error {
	_, err := c.Pool.Exec(context.Background(), schema)
	return err
}

func (c *Cockroach) CreateItem(ctx context.Context, i openapi.Item) (openapi.ImplResponse, error) {
	opts := pgx.TxOptions{}
	tx, err := c.Pool.BeginTx(context.Background(), opts)
	if err != nil {
		return openapi.ImplResponse{}, err
	}
	lang, err := c.GetLanguage(ctx, i.LanguageId)
	if err != nil {
		return openapi.ImplResponse{}, fmt.Errorf("languageId not found")
	}
	i.Id = uuid.New().String()
	defer func() {
		err = tx.Rollback(context.Background())
		if err != nil {
			log.Printf("Error rolling back transaction: %s", err.Error())
		}
	}()

	_, err = tx.Exec(context.Background(),
		"UPSERT INTO helloworld.Items (ID, LanguageId, LanguageName, Value) VALUES ($1,$2,$3,$4)",
		i.Id,
		i.LanguageId,
		(lang.Body).(openapi.Language).Name,
		i.Value,
	)
	i.LanguageName = (lang.Body).(openapi.Language).Name
	if err != nil {
		return openapi.ImplResponse{}, err
	}
	err = tx.Commit(context.Background())
	return openapi.ImplResponse{
		Code: 200,
		Body: i,
	}, err
}

func (c *Cockroach) GetItem(ctx context.Context, id string) (openapi.ImplResponse, error) {
	i := openapi.Item{}
	err := c.Pool.QueryRow(context.Background(),
		"SELECT ID, LanguageId, LanguageName, Value FROM helloworld.Items WHERE ID=$1 LIMIT 1", id).
		Scan(&i.Id, &i.LanguageId, &i.LanguageName, &i.Value)
	if err != nil {
		return openapi.ImplResponse{}, err
	}
	return openapi.ImplResponse{
		Code: 200,
		Body: i,
	}, nil
}

// TODO: when you are done, update the cockroach code in the examples too.

func (c *Cockroach) GetItems(ctx context.Context, id string) (openapi.ImplResponse, error) {
	rows, err := c.Pool.Query(context.Background(),
		"SELECT ID, LanguageId, LanguageName, Value FROM helloworld.Items",
	)
	if err != nil {
		return openapi.ImplResponse{}, err
	}
	defer rows.Close()
	var list []openapi.Item
	for rows.Next() {
		i := openapi.Item{}
		err := rows.Scan(&i.Id, &i.LanguageId, &i.LanguageName, &i.Value)
		if err != nil {
			return openapi.ImplResponse{}, err
		}
		list = append(list, i)
	}
	if len(list) == 0 {
		return openapi.ImplResponse{
			Code: 200,
			Body: make([]string, 0),
		}, nil
	}
	return openapi.ImplResponse{
		Code: 200,
		Body: list,
	}, nil
}

func (c *Cockroach) DeleteItem(ctx context.Context, id string) (openapi.ImplResponse, error) {
	opts := pgx.TxOptions{}
	tx, err := c.Pool.BeginTx(context.Background(), opts)
	if err != nil {
		return openapi.ImplResponse{}, err
	}
	defer func() {
		err = tx.Rollback(context.Background())
		if err != nil {
			log.Printf("Error rolling back transaction: %s", err.Error())
		}
	}()
	_, err = tx.Exec(context.Background(),
		"DELETE FROM helloworld.Items WHERE ID=$1", id)
	err = tx.Commit(context.Background())
	return openapi.ImplResponse{
		Code: 200,
		Body: "OK",
	}, err
}

func (c *Cockroach) UpdateItem(ctx context.Context, id string, item openapi.Item) (openapi.ImplResponse, error) {
	return c.CreateItem(ctx, item)
}

func (c *Cockroach) CreateLanguage(ctx context.Context, l openapi.Language) (openapi.ImplResponse, error) {
	opts := pgx.TxOptions{}
	tx, err := c.Pool.BeginTx(context.Background(), opts)
	if err != nil {
		return openapi.ImplResponse{}, err
	}
	l.Id = uuid.New().String()
	defer func() {
		err = tx.Rollback(context.Background())
		if err != nil {
			fmt.Printf("Error rolling back transaction: %s", err.Error())
		}
	}()
	_, err = tx.Exec(context.Background(),
		"UPSERT INTO helloworld.Languages (ID, Name, Description) VALUES ($1,$2,$3)",
		l.Id,
		l.Name,
		l.Description,
	)
	if err != nil {
		return openapi.ImplResponse{}, err
	}
	err = tx.Commit(context.Background())
	return openapi.ImplResponse{
		Code: 200,
		Body: l,
	}, err
}

func (c *Cockroach) GetLanguage(ctx context.Context, id string) (openapi.ImplResponse, error) {
	i := openapi.Language{}
	err := c.Pool.QueryRow(context.Background(),
		"SELECT ID, Name, Description FROM helloworld.Languages WHERE ID=$1 LIMIT 1", id).
		Scan(&i.Id, &i.Name, &i.Description)
	if err != nil {
		return openapi.ImplResponse{}, err
	}
	return openapi.ImplResponse{
		Code: 200,
		Body: i,
	}, nil
}

func (c *Cockroach) GetLanguages(ctx context.Context) (openapi.ImplResponse, error) {
	rows, err := c.Pool.Query(context.Background(),
		"SELECT ID, Name, Description FROM helloworld.Languages",
	)
	if err != nil {
		return openapi.ImplResponse{}, err
	}
	defer rows.Close()
	var list []openapi.Language
	for rows.Next() {
		i := openapi.Language{}
		err := rows.Scan(&i.Id, &i.Name, &i.Description)
		if err != nil {
			return openapi.ImplResponse{}, err
		}
		list = append(list, i)
	}
	if len(list) == 0 {
		return openapi.ImplResponse{
			Code: 200,
			Body: make([]string, 0),
		}, nil
	}
	return openapi.ImplResponse{
		Code: 200,
		Body: list,
	}, nil
}

func (c *Cockroach) DeleteLanguage(ctx context.Context, id string) (openapi.ImplResponse, error) {
	opts := pgx.TxOptions{}
	tx, err := c.Pool.BeginTx(context.Background(), opts)
	if err != nil {
		return openapi.ImplResponse{}, err
	}
	defer func() {
		err = tx.Rollback(context.Background())
		if err != nil {
			log.Printf("Error rolling back transaction: %s", err.Error())
		}
	}()
	_, err = tx.Exec(context.Background(),
		"DELETE FROM helloworld.Languages WHERE ID=$1", id)
	if err != nil {
		return openapi.ImplResponse{}, err
	}
	_, err = tx.Exec(context.Background(),
		"DELETE FROM helloworld.Items WHERE LanguageId=$1", id)
	err = tx.Commit(context.Background())
	return openapi.ImplResponse{}, err
}

func (c *Cockroach) UpdateLanguage(ctx context.Context, id string, language openapi.Language) (openapi.ImplResponse, error) {
	return c.CreateLanguage(ctx, language)
}
