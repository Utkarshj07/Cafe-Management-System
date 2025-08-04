menu = {
    "PIZZA": 299,
    "BURGER": 79,
    "COFFEE": 69,
    "TEA": 49,
    "SANDWICH": 99,
    "SALAD": 89,
    "MAGGIE": 49
}

print("Welcome to Python Cafe")
print("Menu: \nPizza: Rs299 \nBurger: Rs79 \nCoffee: Rs69 \nTea: Rs49 \nSalad: Rs89 \nSandwich: Rs99 \nMaggie: Rs49")

order_total = 0

item_1 = input("What do you like to have?")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Would you like to have anything else? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available yet!")

print(f"The total number of items to pay is {order_total}")
