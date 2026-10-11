menu = {
    "Burger": 500,
    "Pizza": 800,
    "Fries": 250,
    "Drink": 150
}


def calculate_price(price, quantity):
    return price * quantity


orders = []

while True:
    print("\n----- RESTAURANT MENU -----")
    for item, price in menu.items():
        print(item, "- Rs.", price)

    item_name = input("Enter item name (or 'done' to finish): ").title()

    if item_name == "Done":
        break

    if item_name in menu:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            price = menu[item_name]
            total = calculate_price(price, quantity)

            orders.append({
                "item": item_name,
                "price": price,
                "quantity": quantity,
                "total": total
            })
            print("Added to order.")
        else:
            print("Quantity must be greater than zero.")
    else:
        print("Item not found. Please select an item from the menu.")

grand_total = 0

print("\n----- FINAL BILL -----")
for order in orders:
    print(order["item"], "x", order["quantity"], "= Rs.", order["total"])
    grand_total += order["total"]

print("Total bill: Rs.", grand_total)

with open("orders.txt", "w", encoding="utf-8") as file:
    file.write("----- RESTAURANT BILL -----\n")
    for order in orders:
        file.write(order["item"] + " x " + str(order["quantity"]) +
                   " = Rs. " + str(order["total"]) + "\n")
    file.write("Total bill: Rs. " + str(grand_total) + "\n")

print("Order saved in orders.txt")
