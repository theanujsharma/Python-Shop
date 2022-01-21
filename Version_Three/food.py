import display, order, database

print('Welcome to the shop')
menu = database.food
#prinitng menu 
display.print_list(menu)  # calling the function
#taking order
order.take_order(menu)