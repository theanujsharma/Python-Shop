def take_order(menu):
    order = ""
    order_price = []
    bill = 0
    order_cart = []
    while order != "q":
        order = input("Enter your order press q to quit: - ")
    #checking if order is in menu
        if order in menu:
            print(f"{order} costs ${menu[order]} has been added")
            order_cart.append(order)
            order_price.append(menu[order])
        #when the user says q we are going to print the bill
        elif order == "q":
            name = input("Enter your name: - ")
            print("Thanks for visiting")
            print(f"You have bought these items:-")
            #prining the order cart
            for item in order_cart:
                print(item)
            #calculating bills
            for price in order_price:
                bill = bill + price
            print(f'Your order total is {bill}')
            mybill = open('sales.txt', 'w')
            mybill.write(
                f"{name}, you bought {order_cart} and your total bill is ${bill}")
        else:
            print("Sorry, Its not available")