
products = {
    1: {"name": "Milk", "price": 50},
    2: {"name": "Cheese", "price": 180},
    3: {"name": "Bread", "price": 100},
    4: {"name": "Ice cream", "price": 250},
    5: {"name": "Basmati rice", "price": 400}
}

cart = {}
coupon = ""

while True:
    print("\n1. View Products")
    print("2. Add Product")
    print("3. Remove Product")
    print("4. Update Quantity")
    print("5. Apply Discount")
    print("6. Total Amount")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        for id, item in products.items():
            print(id, item["name"], item["price"])

    elif choice == 2:
        id = int(input("Enter product ID: "))

        if id in products:
            qty = int(input("Enter quantity: "))
            cart[id] = cart.get(id, 0) + qty
            print("Product added")
        else:
            print("Invalid product ID")

    elif choice == 3:
        id = int(input("Enter product ID: "))

        if id in cart:
            del cart[id]
            print("Product removed")
        else:
            print("Product not found in cart")

    elif choice == 4:
        id = int(input("Enter product ID: "))

        if id in cart:
            cart[id] = int(input("Enter new quantity: "))
            print("Quantity updated")
        else:
            print("Product not found in cart")

    elif choice == 5:
        coupon = input("Enter coupon: ")

        if coupon == "SAVE10":
            print("10% Discount applied")
        else:
            coupon = ""
            print("Invalid coupon")

    elif choice == 6:
        total = 0

        for id, qty in cart.items():
            total += products[id]["price"] * qty

        if coupon == "SAVE10":
            total = total * 0.90

        print("Total Amount = Rs.", total)

    elif choice == 7:
        print("Thank you")
        break

    else:
        print("Invalid choice")
