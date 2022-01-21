# menu = ["Pizza", "Burger", "Cookies"]
menu = {"Pizza": 100, "Burger": 200, "Cookies": 300}

#printing menu
def print_menu(menu):
    for item, price in menu.items():
        print(f'{item} ${price}')

#calling the function
print_menu(menu)

#decalaring variables

#taking orders
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
            print("Thanks for visiting")
            print(f"You have  bought these items:-")
            #prining the order cart
            for item in order_cart:
                print(item)
            #calculating bills
            for price in order_price:
                bill = bill + price
            print(f'Your order total is {bill}')
        else:
            print("Sorry, Its not available")

take_order(menu)