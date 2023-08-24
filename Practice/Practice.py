name=input("What is your name? ")
length= len(name)
print(length)
##Project 1
#1. Create a greeting for your program.
print("Welcome to the Band Name Generator")
#2. Ask the user for the city that they grew up in.
name_of_city = input("What is the name of the city you grew in ? \n")
#3. Ask the user for the name of a pet.
name_of_pet = input("What is the name of your pet ? \n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be "+name_of_city + " " + name_of_pet )

score= 3
height = 1.23
name= "Adiam"
winning = True
print(f"The player name is {name} whose height is {height} has a score of {score} and is winning{winning}")

print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
percentage_tip = input("what percentage of tip would you like to give 10,12 or 15? ")
converted_percenatge_bill = int(percentage_tip)/100+1
Split= input("How many people to split the bill ? ")
total_bill = float(bill)*float(converted_percenatge_bill)
rounded_bill = round(total_bill,2)
print(f"Each person has to pay ${rounded_bill/int(Split)}")