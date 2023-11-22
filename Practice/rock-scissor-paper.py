import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("what do you choose? Type 0 for Rock 1 for paper 2 for Scissors.\n"))
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
else:
  print(input("please retry again.Type 0 for Rock 1 for paper 2 for Scissors.\n"))

Computer_chose = random.randint(0,2)
if Computer_chose == 0:
  print(rock)
elif Computer_chose == 1:
  print(paper)
elif Computer_chose == 2:
  print(scissors)

if choice == 0 and Computer_chose== 1:
  print("You lose")
elif choice == 1 and Computer_chose== 2:
  print("You lose")
elif choice == 2 and Computer_chose== 0:
  print("You lose")
elif choice == 1 and Computer_chose== 0:
  print("You Win")
elif choice == 2 and Computer_chose== 1:
  print("You Win")
elif choice == 0 and Computer_chose== 2:
  print("You Win")
elif choice==Computer_chose:
    print("Its a draw.")
else:
    print("You piceked a invalid choice. You lose.")