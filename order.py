'''
Order
'''
from pizzaReceipt import generateReceipt

# constant tuple holding all topping options
TOPPINGS = ("ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH",
            "BROCCOLI", "PINEAPPLE", "HOT PEPPER", "PEPPERONI", "HAM", "BACON", "GROUND BEEF",
            "CHICKEN", "SAUSAGE")
# constant tuple holding all size options
SIZES = ("S", "M", "L", "XL")
# empty list that will hold all the toppings the user inputs
toppingList = []
# input the entire order, if empty return that there is no order
pizzaOrder = []
# first time asking
firstAsk = input("Do you want to order a pizza? ")
if firstAsk.lower() == "q" or firstAsk.lower() == 'no':
    wantToOrder = False
# loop that will continue making pizzas and inputting into whole order
else:
    # to exit the loop of creating new pizzas
    wantToOrder = True
    while wantToOrder:
        # first ask size
        pizzaSize = input("Choose a size: S, M, L, XL: ").upper()
        # loop to make sure size entered is valid
        while pizzaSize not in SIZES:
            pizzaSize = input("Choose a size: S, M, L, XL: ").upper()
        if pizzaSize in SIZES:
            size = pizzaSize.upper()

        doneToppings = False
        # loop to evaluate toppings entered each time and respond accordingly
        while not doneToppings:
            # ask user to enter toppings
            toppingChoice = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"\n('")
            # prints list of topping options
            if toppingChoice.upper() == "X":
                doneToppings = True
            elif toppingChoice.upper() == "LIST":
                print(TOPPINGS)
            # add topping to list of toppings if valid
            elif toppingChoice.upper() in TOPPINGS:
                toppingList.append(toppingChoice.upper())
            # make sure topping entered is valid
            elif toppingChoice.upper() not in TOPPINGS:
                print("Invalid topping")

        # create a tuple containing the size and list to be added to entire order
        pizzaItem = (size, toppingList)
        pizzaOrder.append(pizzaItem)

        askOrder = input("Do you want to continue ordering? ")
        if askOrder.lower() == "q" or askOrder.lower() == 'no':
            wantToOrder = False
        else:
            wantToOrder = True
# return order
if not wantToOrder:
    generateReceipt(pizzaOrder)