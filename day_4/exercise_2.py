# Who's Paying
# Instructions
# You are going to write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# Line 8 splits the string names_string into individual names and puts them inside a List called names. 
# For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name
# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.
# Example Output
# Michael is going to buy the meal today!
# Note: Remember that Lists start at index 0!
# import random
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
# nameAsCSV = input("Give me everybody's names, separated by a comma ")
# names = nameAsCSV.split(" , ")
# num_items = len(names)
# random_choice = random.randint(0, num_items -1)
# person_who_will_pay = names[random_choice]
# print(f"person_who_will_pay is going to buy the meal today!")
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
num_items = len(names)
random_choice = random.randint(1, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today.")
