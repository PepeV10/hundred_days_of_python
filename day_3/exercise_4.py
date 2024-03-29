# Pizza Order
# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program. 
# Based on a user's order, work out their final bill.
# Prices: 
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.
print("Welcome to Pepe's Pizzeria!")
size = input("What size pizza do you want? Small - S, Medium - M, Large - L: ")
add_pepperoni = input("Do you want Pepperoni? Yes - Y, or No - N: ")
extra_cheese = input("Do you want extra cheese? Yes - Y, or No - N: ")
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25
if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
if extra_cheese == "Y":
  bill += 1
print(f"Your final bill is: ${bill}")
