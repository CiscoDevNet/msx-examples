import pprint


class Language:
	def __init__(self, id=None, name=None, description=None):
		self._id = id
		self._name = name
		self._description = description

	def to_dict(self):
		return {
			"id": self._id,
			"name": self._name,
			"description": self._description
		}

	def to_str(self):
		return pprint.pformat(self.to_dict())

	def __repr__(self):
		return self.to_str()