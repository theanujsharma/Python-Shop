class Shop:
    order = ""
    order_price = []
    bill = 0
    order_cart = []
    def __init__(self, menu):
        self.menu = menu
    
    def print_menu(self):
        for item, price in self.menu.items():
            print(f'{item} ${price}')

    def taking_orders(self):
        while self.order != "q":
            self.order = input("Enter your order press q to quit: - ")
        # checking if order is in menu
            if self.order in self.menu:
                print(f"{self.order} costs ${self.menu[self.order]} has been added")
                self.order_cart.append(self.order)
                self.order_price.append(self.menu[self.order])

            # when the user says q we are going to print the bill
            elif self.order == "q":
                print("Thanks for visiting")
                print(f"You have  bought these items:-")
                # prining the order cart
                for item in self.order_cart:
                    print(item)
                # calculating bills
                for price in self.order_price:
                    self.bill = self.bill + price
                print(f'Your order total is {self.bill}')
            else:
                print("Sorry, Its not available")


food = Shop({"Pizza": 100, "Burger": 200, "Cookies": 300})
food.print_menu()
food.taking_orders()

