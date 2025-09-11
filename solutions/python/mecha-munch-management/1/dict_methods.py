"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        current_cart[item] = current_cart.get(item,0) +1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    current_cart = dict()
    for item in notes:
        current_cart[item] = current_cart.get(item,0) +1
    return current_cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    new_idea = dict(recipe_updates)
    ideas.update(new_idea)
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return sorted(cart.items())


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    fulfillement_cart = {}
    for item, qty in cart.items(): 
        fulfillement_cart[item] = [qty] + aisle_mapping[item]
        
    return dict(sorted(fulfillement_cart.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    updated_inventory = store_inventory.copy()
    for item, qty in fulfillment_cart.items(): 
        order_qty = qty[0]
        stock_qty = store_inventory[item][0]

        remaining = stock_qty - order_qty
        if remaining <= 0:
            store_inventory[item][0] = 'Out of Stock'
        else:
            updated_inventory[item][0] = remaining
    return updated_inventory
