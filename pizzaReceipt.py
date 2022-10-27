'''
Receipt
'''
def generateReceipt(pizzaOrder):
    # if pizza order is empty exit function
    if len(pizzaOrder) == 0:
        print("You did not order anything")
        return

    # if pizza order is not empty print a receipt
    else:
        count = 1
        totalCost = float(0)
        print("Your order: ")
        for e in pizzaOrder:
            # assign prices
            totalCost += pricing(e[0], "base")
            # print out the pizza number, size, and initial price
            if e[0] == "XL":
                print("Pizza %d: %s %19.2f" % (count, e[0], pricing(e[0], "base")))
            else:
                print("Pizza %d: %s %20.2f" % (count, e[0], pricing(e[0], "base")))

            # if topping list is within 3
            if len(e[1]) <= 3:
                for i in range(len(e[1])):
                    print("- %s" % (e[1][i]))

            # if topping list is over 3
            if len(e[1]) > 3:
                for i in range(3):
                    print("- %s" % (e[1][i]))
                x = len(e[1]) - 3
                totalCost += (pricing(e[0], "extra") * x)
                for p in range(4, len(e[1]) + 1):
                    print("- %s" % (e[1][p - 1]))
                for q in range(x):
                    if e[0] == "XL":
                        print("Extra Topping (%s) %12.2f" % (e[0], pricing(e[0], "extra")))
                    else:
                        print("Extra Topping (%s) %13.2f" % (e[0], pricing(e[0], "extra")))

            # increase count
            count += 1

        # print tax and new total after tax
        tax = float(totalCost * 0.13)
        print("Tax: %26.2f" % tax)
        totalCost += tax
        print("Total: %24.2f" % totalCost)

# for each size assign the base cost and additional topping cost
def pricing(sizing, priceType):
    if priceType == "base":
        if sizing == "S":
            initialCost = 7.99
            return initialCost
        elif sizing == "M":
            initialCost = 9.99
            return initialCost
        elif sizing == "L":
            initialCost = 11.99
            return initialCost
        elif sizing == "XL":
            initialCost = 13.99
            return initialCost

    if priceType == "extra":
        if sizing == "S":
            extraToppingCost = 0.5
            return extraToppingCost
        elif sizing == "M":
            extraToppingCost = 0.75
            return extraToppingCost
        elif sizing == "L":
            extraToppingCost = 1
            return extraToppingCost
        elif sizing == "XL":
            extraToppingCost = 1.25
            return extraToppingCost