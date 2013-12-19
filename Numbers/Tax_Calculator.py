#**Tax Calculator**
#Asks the user to enter a cost and either a country or state tax.
#It then returns the tax plus the total cost with tax.

price = 0
tax = 0
total = 0

price = input("Input cost of item: ")
tax = input("Input decimal equivalent of tax rate: ")

total = price + (price * tax)

print("Total price is: " + str(total))