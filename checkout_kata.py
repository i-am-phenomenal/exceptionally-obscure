# CHECKOUT KATA

# --------FUNCTIONS SECTIONS START HERE-------------

def get_distinct_items(items):
    items_dict = {}
    for item in items:
        items_dict[item] = items.count(item)
    return items_dict

def get_unit_price_remainder(value, item_quantity):
    if value == "A": 
        return item_quantity % 3

    else: 
        return item_quantity % 2

def get_special_price(value, item_quantity):
    if value == "A": 
        return int(item_quantity / 3) * 130
    else:
        return int(item_quantity / 2) * 45

def return_cost_for_current_item(items_dict, value):
    global item_prices 
    special_price = get_special_price(value, items_dict[value])
    unit_price_remainder = get_unit_price_remainder(value, items_dict[value])
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
        if value == "A" and items_dict[value] >= 3:
            total_cost += return_cost_for_current_item(items_dict, "A")

        elif value == "B" and items_dict[value] >= 2:
            total_cost += return_cost_for_current_item(items_dict, "B")

        else:
            total_cost += items_dict[value] * item_prices[value]

    return total_cost


def get_all_prices(items):
    cost_list = []
    for item in items:
        cost_list.append(calculate_price(item))
    return cost_list

# --------------- FUNCTIONS SECTION ENDS HERE -----------

items = ["", "A", "AB", "CDBA", "AA", "AAA", "AAAA",
         "AAAAA", "AAAAAA", "AAAB", "AAABB", "AAABBD", "DABABA"]
item_prices = {"A": 50, "B": 30, "C": 20, "D": 15}

print("OUTPUT -> ", get_all_prices(items))


# ----------- TEST CASES --------------

def test_item_count():
    user_items = "ABAABBA" # Created Dummy Data
    items_dictionary = get_distinct_items(user_items)
    assert (items_dictionary["A"] == 4) and (items_dictionary["B"] == 3), "Count of A should be 4 and count of B should be 3"


def test_cost_for_current_item():
    user_items = "AACDACBABBBBBCABB"
    # Cost for A should be 230 and cost for B should be 180
    items_dictionary = get_distinct_items(user_items)
    cost_for_A = return_cost_for_current_item(items_dictionary, "A")
    cost_for_B = return_cost_for_current_item(items_dictionary, "B")
    assert (cost_for_A == 230 and cost_for_B == 180), "Cost for A should be 230 and cost for B should be 180"

def test_total_price_per_customer():
    customer_items = "AACDACBABBBBBCABB"
    #  Total price for this customer would be 485
    total_price = calculate_price(customer_items)
    assert total_price == 485, "Total cost that this customer has to pay for these items should be calculated as 485"

def test_prices_for_all_users():
    all_user_items = ["", "", "ABCDABBABA", "DCDCDDDCDCD", "BBABBACD"]
    # The cost for the above users should be [0, 0, 305, 185, 225]
    all_prices = get_all_prices(all_user_items)
    assert all_prices == [0, 0, 305, 185, 225], "Correct cost should be returned for all users "

if __name__ == "__main__":
    test_item_count()
    test_cost_for_current_item()
    test_total_price_per_customer()
    test_prices_for_all_users()
    print("All test cases have passed :)")
