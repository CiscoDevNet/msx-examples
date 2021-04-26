# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from hello_world_service.models.error import Error  # noqa: E501
from hello_world_service.models.language import Language  # noqa: E501
from hello_world_service.test import BaseTestCase


class TestLanguagesController(BaseTestCase):
    """LanguagesController integration test stubs"""

    def test_create_language(self):
        """Test case for create_language

        Creates a new langauge.
        """
        language = {
  "name" : "name",
  "description" : "description",
  "id" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/helloworld/api/v1/languages',
            method='POST',
            headers=headers,
            data=json.dumps(language),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_language(self):
        """Test case for delete_language

        Deletes a langauge.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/helloworld/api/v1/languages/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_language(self):
        """Test case for get_language

        Returns a language.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/helloworld/api/v1/languages/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_languages(self):
        """Test case for get_languages

        Returns a list of languages.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/helloworld/api/v1/languages',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_language(self):
        """Test case for update_language

        Updates a langauge.
        """
        language = {
  "name" : "name",
  "description" : "description",
  "id" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/helloworld/api/v1/languages/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(language),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
