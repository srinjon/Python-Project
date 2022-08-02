import random
from turtle import pos, position
import my_module
# random_integer=random.randint(1, 10)
# print(random_integer)
# print(my_module.pi)
# random_float=round(random.random()*5,2)
# print(random_float)
# loveCalculator = str(random.randint(1,100))
# if (int(loveCalculator)<10) or (int(loveCalculator)>90):
#     print("Your love Score is " +loveCalculator+ ", You go together like coke and mentos")
# elif (int(loveCalculator)>=40) and (int(loveCalculator)<=50):
#     print("Your love Score  is "+loveCalculator+", you are alright together")
# else:
#     print("Your love Score is "+loveCalculator)
# 4.2
# coin=round(random.randint(0,1))
# if coin==1:
#     print("Heads")
# else:
#     print("Tails")
# 3.3
India_states1 = ["WestBengal","TamilNadu","Gujrat","Delhi","Rajasthan"]
India_states2 = ["Tripura","Assam","Mizoram","Goa","Kerala"]
India_states = [India_states1,India_states2]
find = len(India_states1)
print(India_states1[find-1])
print(India_states)
print(India_states[1][1])
# print(India_states)
# print(India_states[1])
# print(India_states[-1])
# India_states[0] = "Bengal"
# print(India_states)
# India_states.append("Kerala")
# print(India_states)
# India_states.extend(["Assam","Tripura"])   
# print(India_states)
# 3.4
# name_string = input("Give me everybody's names,seperated by a comma. ")
# names = name_string.split(", ")
# num_items = len(names)
# random_choice = random.randint(0, num_items-1)
# person=names[random_choice]
# person = random.choice(names)
# print(f"{person} is going to buy the meal today!")
row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position =input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])
map[vertical-1][horizontal-1]="X"
print(f"{row1}\n{row2}\n{row3}")


