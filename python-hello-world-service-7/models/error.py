#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#
class Error:
    def __init__(self, code=None, message=None):
        self._code = code
        self._message = message

    def to_dict(self):
        return {
            "code": self._code,
            "message": self._message,
        }
