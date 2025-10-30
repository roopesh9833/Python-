Name =  input("Enter the name ")

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

Paper =  '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
Scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

Game_mode = [Rock , Paper ,Scissor ]

# print(Game_mode[0])

User_choice = int(input(" enter your choice 0 Rock , 1 paper , 2 Scissor "))

if User_choice < 0 or User_choice >2:
   print("kindly enter Valid number you must select either 0 , 1 or 2  ")
   exit()

print (Name," you choosed ",(Game_mode[User_choice]))

import random

Cpu_Choice = random.randint(0,2)
CPU_choosed  =  Game_mode [Cpu_Choice]
print ("CPU Choosed ",(CPU_choosed))


if User_choice == Cpu_Choice:
   print("Draw") 
elif User_choice == 0 and  Cpu_Choice == 2:
   print(Name,"you won ")
elif User_choice == 0 and Cpu_Choice == 1:
   print(Name,"oops you lose")
elif User_choice == 1 and Cpu_Choice == 0:
   print(Name,"you won ")
elif User_choice == 1 and Cpu_Choice == 2:
   print(Name,"oops you lose")
elif User_choice == 2 and Cpu_Choice == 1:
    print(Name,"you won ")
elif User_choice == 2 and Cpu_Choice == 0:
   print(Name,"you lose ")
      
