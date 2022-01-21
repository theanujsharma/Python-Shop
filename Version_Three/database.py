#hard coded
myMenu = open("menu.csv", "r") # Open the menu file
myList = myMenu.readlines()    # Read the menu file, this will save my data in a list.
mydictionary = {}              # Create an empty dictionary
for line in myList[1:]:
    myLine = (line.strip().split(","))   
    item = myLine[0]  
    price = myLine[1]     # Print the list
    mydictionary[item] = int(price)  # Add the list to the dictionary
food = mydictionary 