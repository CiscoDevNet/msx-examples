import connexion
import six

from hello_world_service.models.error import Error  # noqa: E501
from hello_world_service.models.language import Language  # noqa: E501
from hello_world_service import util

LANGUAGE_ENGLISH = Language(
    id="01f643a5-7e34-4366-af1a-9cce5e5c68e8",
    name="English",
    description="A West Germanic language that uses the Roman alphabet.")


LANGUAGE_RUSSIAN = Language(
    id="55f3028f-1b94-4edd-b14f-183b51b33d68",
    name="Russian",
    description="An East Slavic language that uses the Cyrillic alphabet.")


def create_language(language):  # noqa: E501
    """Creates a new langauge.

     # noqa: E501

    :param language: 
    :type language: dict | bytes

    :rtype: Language
    """
    if connexion.request.is_json:
        language = Language.from_dict(connexion.request.get_json())  # noqa: E501
    return LANGUAGE_ENGLISH


def delete_language(language_id):  # noqa: E501
    """Deletes a langauge.

     # noqa: E501

    :param language_id: 
    :type language_id: 

    :rtype: None
    """
    return 'do some magic!'


def get_language(language_id):  # noqa: E501
    """Returns a language.

     # noqa: E501

    :param language_id: 
    :type language_id: 

    :rtype: Language
    """
    return LANGUAGE_ENGLISH


def get_languages():  # noqa: E501
    """Returns a list of languages.

     # noqa: E501


    :rtype: List[Language]
    """
    return [LANGUAGE_ENGLISH, LANGUAGE_RUSSIAN]


def update_language(language_id, language):  # noqa: E501
    """Updates a langauge.

     # noqa: E501

    :param language_id: 
    :type language_id: 
    :param language: 
    :type language: dict | bytes

    :rtype: Language
    """
    if connexion.request.is_json:
        language = Language.from_dict(connexion.request.get_json())  # noqa: E501
    return LANGUAGE_ENGLISH
