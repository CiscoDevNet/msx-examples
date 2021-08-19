#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All rights reserved
#
class Language:
	def __init__(self, id=None, name=None, description=None, row=None):
		if row:
			self._id = row["id"]
			self._name = row["name"]
			self._description = row["description"]
		else:
			self._id = id
			self._name = name
			self._description = description

	def to_dict(self):
		return {
			"id": self._id,
			"name": self._name,
			"description": self._description
		}