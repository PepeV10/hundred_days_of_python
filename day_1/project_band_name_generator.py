#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/

print("Welcome to Pepe's Awesome Band Name Generator!\n")
city_name = input("What is the name of the City you grew up in?\n")
pet_name = input("What is the name of your first pet?\n")
print("Congratulations, the name of your Brand New Awesome Band is:\n" "The " + city_name + " " + pet_name)