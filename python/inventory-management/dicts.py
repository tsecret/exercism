"""Functions to keep track and alter inventory."""

from typing import List, Dict

def create_inventory(items: List[str]):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    d = {}

    for item in items:
      if item not in d:
        d[item] = 1
      else:
        d[item] += 1

    return d


def add_items(inventory: Dict[str, int], items: List[str]):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    for item in items:
      if item not in inventory:
        inventory[item] = 1
      else:
        inventory[item] += 1

    return inventory


def decrement_items(inventory: Dict[str, str], items: List[str]):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """


    for item in items:
      if item not in inventory:
        continue

      if inventory[item] >= 1:
        inventory[item] -= 1

    return inventory


def remove_item(inventory: Dict[str, int], item: str):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    if item not in inventory:
      return inventory

    inventory.pop(item)
    return inventory


def list_inventory(inventory: Dict[str, int]):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [(item, qty) for item, qty in inventory.items() if qty > 1]
