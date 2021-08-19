#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
class Item:
	def __init__(self, id=None, language_id=None, language_name=None, value=None, row=None):
		if row:
			self._id = row.get("id", None)
			self._language_id = row.get("languageid", None)
			self._language_name = row.get("languagename", None)
			self._value = row.get("value", None)
		else:
			self._id = id
			self._language_id = language_id
			self._language_name = language_name
			self._value = value

	def to_dict(self):
		return {
			"id": self._id,
			"languageId": self._language_id,
			"languageName": self._language_name,
			"value": self._value
		}

