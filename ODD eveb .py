
# User_Choice = int(input("Select the number the number  from 1 to 5 :  "))

# if User_Choice  < 1 or User_Choice > 5:
#     print ("kinldy enter valid range form 1 t 5 ")
#     exit()
# elif User_Choice % 2 == 0:
#     print ("Even")
# elif User_Choice % 2 != 0:
#     print ("odd")
# print ("Your choice ", User_Choice)

# import random

# CPU_Choice = random.randint(1,5)

# print ("CPU choosed  ", CPU_Choice)
# Total_Score =  (User_Choice + CPU_Choice)

# if Total_Score % 2 == 0:
#     print odd


# def retry():
#     User_Choice = int(input("Select the number the number  from 1 to 5 :  "))

#     if User_Choice <1 or User_Choice >5:    
#         print ("kindly enter the vaild number ")
#         retry ()
#     else :
#         print("welocme to the game ")




# def retry():
#     User_Choice = int(input("Select the number from 1 to 5: "))

#     if User_Choice < 1 or User_Choice > 5:
#         print("❌ Kindly enter a valid number!")
#         retry()  # recursion, dobara function call
#     else:
#         print("✅ You entered:", )

# # Function call
# retry()


# Tumhara sawaal bahut accha hai! Kyunki tumne Rock, Paper, Scissors (RPS) ka logic itni acchi tarah se samajh liya hai, isliye ab us par based ek naya game solve karna aur bhi mazedar hoga.

# Main tumhe "RPS ke jaisa hi" ek naya aur famous game deta hoon jismein if/elif/else ka pura use hoga: Odd or Even (Jise hum Hindi mein 'Aka-Baka' ya 'Chheen-Chhappa' bhi kehte hain).

# 🎯 Naya Sawaal: Odd or Even Game Logic
# Yeh game RPS se thoda simple hai, lekin ismein bhi if/elif/else ka use hota hai.

# Rules of the Game:

# Choice: User choose karta hai ki unka Total Score Odd hoga ya Even.

# User ka Number: User 1 se 5 tak koi bhi number select karta hai.

# Computer ka Number: Computer bhi 1 se 5 tak koi random number select karta hai.

# Total Score: Dono numbers ko joda jaata hai.

# Result: Check kiya jaata hai ki Total Score Odd hai ya Even.



import random 

user_choice = int(input("enter the you number "))
CPU = random.randint(1,5)

if user_choice < 1 or  user_choice > 5 :
    print("kindly enter valid number 1 to 5 ")
    exit ()
total = user_choice + CPU

print(user_choice)
print("Cpu choosed number ",CPU)
print(f"total", total)

Odd_Even  = total % 2

# if Odd_Even == 0 and user_choice == 0:
#     if Odd_Even == 1 and user_choice == 1:
#         print("you won ")
# elif Odd_Even == 1 and user_choice == 0:
#     if Odd_Even == 0 and user_choice == 1:
#         print("you old")
    
if Odd_Even == 0 and user_choice == 0:
    print("🎉 You win! Total is Even.")
elif Odd_Even == 1 and user_choice == 1:
    print("🎉 You win! Total is Odd.")
else:
    print("😢 You lose!")
        





