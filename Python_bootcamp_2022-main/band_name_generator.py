#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end

print("Hey there! Welcome to Bruno's Band Name Generator")
city_name = input("What's name of the city you grew up in\n?")
print(city_name)
pet_name = input("what's your pet's name\n?")
print(pet_name)
print("Your band name could be " + city_name + pet_name )