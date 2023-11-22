import time
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
time.sleep(3)
print("Your mission is to find the treasure.") 

answer = input("Are you ready?")
time.sleep(3)
print(f"{answer} ? , well its only one way to find out")
time.sleep(2)
print("You have to start your journey now. Take the motorbike by yourself or wait for the car to go with the group.")
answer_1 = input("Type 'M' for motorbike or 'C' for Car: ")

if answer_1.lower() == "m":
    print("Well done, youngblood, to live is not to fear being alone")
    time.sleep(2)
    print("You passed level one. Would you like to party?")
    answer_2 = input("Type 'Y' for yes or 'N' for No: ")
    time.sleep(4)
    
    if answer_2.lower() == "y":
        print("A little party doesn't hurt...")
    elif answer_2.lower() == "n":
        print("What a shame, you were doing so good")
        time.sleep(2)
        print("Don't take life seriously. You can't get out of it alive anyhow")
    else:
        print("Invalid input for the party decision.")

elif answer_1.lower() == "c":
    print("My young one, don't fear going on this journey, but for now, your time ends here.")
else:
    print("Invalid input for the vehicle choice.")