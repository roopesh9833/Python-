# print ("hello world ")    #   --------> print finctuon  and "hello world " is a fucntion 
# print ("hello \n World ")   #  -------->  \n new line 

# -----------------------------------------------Cocatinate----------------------------------------------


# a = ("Apple") 
# b = ("Grapes")
# print( a + b )   --------> # concatination 
# print( a +  " " + b  )    --------> concatinate with space 


# -----------------------------------------------Variable ----------------------------------------------


# a = 10     # a is a variable to store value 
# print (a)

#---------------------------------------------------Input Method --------------------------------

# print("hello " + " " + "Angela")
# a = input("enter your age ")
# print("woow!! you are so young " + a)

#






#-----------------------------------------------------F string BMI round  ----------------------------------
# bmi = 84 / 1.65 ** 2

# height = 6.5
# weight = "80"

# #print (f" your height is  {height}  your formal is  {formal} ")

# weightCOnv = int(weight)

# bmi = (f"your bmi " , round ( weightCOnv / height **2))

# print  (bmi)

# ---------------------------------------------------

# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))
#
# from subprocess import Popen

# # Bill =int(input(" enter your total Bill  = "))
# # tip = int(input(" Chose your Tip you wanted to provide 10% 12% or 15%  = "))
# # People =  int(input("How many pople to be contribute "))

# # tipCal = (tip/100 * Bill)
# # cal = (Bill + tipCal)
# # final = (cal / People)

# # print (final)

# #/----------------------------------------------------

# print("welcome to INOX")
# Age = int(input("enter the Age "))
# if Age < 12:
#     print ("your ticket price is 5 $")
# else:
#     if Age < 18 :
#         print("your ticket price is 7 $")
#     else:
#         print ("your ticket price is 12 $")


# import random

# CPU = random.randint(0,2)

# print(CPU)




# User_choice = int(input(" enter your choice 0 Rock , 1 paper , 2 Scissor "))

# if User_choice < 0 or User_choice >2:
#    print("kindly enter Valid number you must select either 0 , 1 or 2  ")
#    exit()
# else:
#    print("bingoo")


# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# # Note: it's worth checking if the user has made a valid choice before the next line of code.
# # If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# # You could for example write:
# if user_choice >= 0 and user_choice <= 2:
#     print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number. You lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose!")
# elif computer_choice > user_choice:
#     print("You lose!")
# elif user_choice > computer_choice:
#     print("You win!")
# elif computer_choice == user_choice:
#     print("It's a draw!")




# User_Choice = int(input("Select the number the number  from 1 to 5 :  "))

# if User_Choice  < 1 or User_Choice > 5:
#     print ("kinldy enter valid range form 1 t 5 ")
#     exit()
# elif User_Choice % 2 == 0:
#     print ("Even")
# elif User_Choice % 2 != 0:
#     print ("odd")\
# Total_Score = 3
# print ("even"if Total_Score % 2 == 0 or "odd" else "odd")

# Game_mode = ["Rock" , "Paper" ,"Scissor "]

# print (Game_mode[0])




User_Choice = int(input("Select the number the number  from 1 to 5 :  "))

if User_Choice  < 1 or User_Choice > 5:
    print ("kinldy enter valid range form 1 t 5 ")
    exit()
elif User_Choice % 2 == 0:
    print ("Even")
elif User_Choice % 2 != 0:
    print ("odd")
print ("Your choice ", User_Choice)

if User_Choice == "Even": 
    print("you win")
else:
    print("odd")
