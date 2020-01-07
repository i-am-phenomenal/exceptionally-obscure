# CHECKOUT KATA


def get_distinct_items(items):
    items_dict = {}
    for item in items:
        items_dict[item] = items.count(item)
    return items_dict


def return_cost_for_A(items_dict, value):
    global item_prices
    special_price = int(items_dict[value] / 3) * 130
    unit_price_remainder = items_dict[value] % 3
    if unit_price_remainder == 0:
        return special_price
    else:
        unit_price = (unit_price_remainder * item_prices[value])
        return (special_price + unit_price)


def return_cost_for_B(items_dict, value):
    global item_prices
    special_price = int(items_dict[value] / 2) * 45
    unit_price_remainder = items_dict[value] % 2
    if unit_price_remainder == 0:
        return special_price
    else:
        unit_price = (unit_price_remainder * item_prices[value])
        return (special_price + unit_price)


def calculate_price(items):
    global item_prices
    total_cost = 0
    items_dict = get_distinct_items(items)
    for value in items_dict:
        if value == "a" and items_dict[value] >= 3:
            print("I am here")
            total_cost += return_cost_for_A(items_dict, value)

        elif value == "b" and items_dict[value] >= 2:
            total_cost += return_cost_for_B(items_dict, value)

        else:
            total_cost += items_dict[value] * item_prices[value]

    return total_cost


items = "dababa"
item_prices = {"a": 50, "b": 30, "c": 20, "d": 15}

print(calculate_price(items), "TOTAL COST")
