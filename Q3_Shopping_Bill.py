def calculate_bill(products):
    subtotal = 0
    for product in products:
        product["total"] = product["price"] * product["quantity"]
        subtotal += product["total"]

    discount = 0
    if subtotal > 10000:
        discount = subtotal * 0.10

    final_bill = subtotal - discount
    return subtotal, discount, final_bill


products = []

for i in range(5):
    print("\nProduct", i + 1)
    name = input("Enter product name: ")
    price = float(input("Enter price: Rs. "))
    quantity = int(input("Enter quantity: "))

    products.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

subtotal, discount, final_bill = calculate_bill(products)

most_expensive = products[0]
for product in products:
    if product["price"] > most_expensive["price"]:
        most_expensive = product

print("\n--------- SHOPPING BILL ---------")
for product in products:
    print(product["name"], "- Rs.", product["price"],
          "x", product["quantity"], "=", product["total"])

print("Subtotal: Rs.", subtotal)
print("Discount: Rs.", discount)
print("Final bill: Rs.", final_bill)
print("Most expensive product:", most_expensive["name"])

with open("bill.txt", "w", encoding="utf-8") as file:
    file.write("--------- SHOPPING BILL ---------\n")
    for product in products:
        file.write(product["name"] + " - Rs. " + str(product["price"]) +
                   " x " + str(product["quantity"]) + " = Rs. " +
                   str(product["total"]) + "\n")
    file.write("Subtotal: Rs. " + str(subtotal) + "\n")
    file.write("Discount: Rs. " + str(discount) + "\n")
    file.write("Final bill: Rs. " + str(final_bill) + "\n")
    file.write("Most expensive product: " + most_expensive["name"] + "\n")

print("Bill saved in bill.txt")
