# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from hello_world_service.models.error import Error  # noqa: E501
from hello_world_service.models.item import Item  # noqa: E501
from hello_world_service.test import BaseTestCase


class TestItemsController(BaseTestCase):
    """ItemsController integration test stubs"""

    def test_create_item(self):
        """Test case for create_item

        Creates a new Hello World item.
        """
        item = {
  "languageId" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
  "id" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
  "languageName" : "languageName",
  "value" : "value"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/helloworld/api/v1/items',
            method='POST',
            headers=headers,
            data=json.dumps(item),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_item(self):
        """Test case for delete_item

        Deletes a Hello World item.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/helloworld/api/v1/items/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_item(self):
        """Test case for get_item

        Returns a Hello World item.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/helloworld/api/v1/items/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_items(self):
        """Test case for get_items

        Returns a list of Hello World items.
        """
        query_string = [('languageId', 'language_id_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/helloworld/api/v1/items',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_item(self):
        """Test case for update_item

        Updates a Hello World item.
        """
        item = {
  "languageId" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
  "id" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
  "languageName" : "languageName",
  "value" : "value"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/helloworld/api/v1/items/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(item),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
