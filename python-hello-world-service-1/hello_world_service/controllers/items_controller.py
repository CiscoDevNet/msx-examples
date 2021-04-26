import connexion
import six

from hello_world_service.models.error import Error  # noqa: E501
from hello_world_service.models.item import Item  # noqa: E501
from hello_world_service import util

HELLO_WORLD_ENGLISH = Item(
    id="68963944-a88c-4e39-98fd-d77878231d81",
    language_id="01f643a5-7e34-4366-af1a-9cce5e5c68e8",
    language_name="English",
    value="Hello, World!")

HELLO_WORLD_RUSSIAN = Item(
    id="62ef8e5f-628a-4f8b-92c9-485981205d92",
    language_id="55f3028f-1b94-4edd-b14f-183b51b33d68",
    language_name="Russian",
    value="Привет мир!")


def create_item(item):  # noqa: E501
    """Creates a new Hello World item.

     # noqa: E501

    :param item: 
    :type item: dict | bytes

    :rtype: Item
    """
    if connexion.request.is_json:
        item = Item.from_dict(connexion.request.get_json())  # noqa: E501
    return HELLO_WORLD_ENGLISH


def delete_item(item_id):  # noqa: E501
    """Deletes a Hello World item.

     # noqa: E501

    :param item_id: 
    :type item_id: 

    :rtype: None
    """
    return 'do some magic!'


def get_item(item_id):  # noqa: E501
    """Returns a Hello World item.

     # noqa: E501

    :param item_id: 
    :type item_id: 

    :rtype: Item
    """
    return HELLO_WORLD_ENGLISH


def get_items(language_id=None):  # noqa: E501
    """Returns a list of Hello World items.

     # noqa: E501

    :param language_id: 
    :type language_id: 

    :rtype: List[Item]
    """
    return [HELLO_WORLD_ENGLISH, HELLO_WORLD_RUSSIAN]


def update_item(item_id, item):  # noqa: E501
    """Updates a Hello World item.

     # noqa: E501

    :param item_id: 
    :type item_id: 
    :param item: 
    :type item: dict | bytes

    :rtype: Item
    """
    if connexion.request.is_json:
        item = Item.from_dict(connexion.request.get_json())  # noqa: E501
    return HELLO_WORLD_ENGLISH
