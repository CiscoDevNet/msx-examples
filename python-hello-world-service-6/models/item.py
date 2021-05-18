class Item:
	def __init__(self, id=None, language_id=None, language_name=None, value=None):
		self._id = id
		self._language_id = language_id
		self._language_name = language_name
		self._value = value

	def to_dict(self):
		return {
			"id": self._id,
			"language_id": self._language_id,
			"language_name": self._language_name,
			"value": self._value
		}