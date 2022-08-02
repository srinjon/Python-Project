# 3.1
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height(cm)? "))
# if height>=120:
#      print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
# 3.2
# number = int(input());
# if number%2==0:
#     print("Even")
# else:
#     print("Odd")
# 3.3
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height(cm)? "))
# if height>=120:
#      print("You can ride the rollercoaster!")
#      age = int(input("Put you age for price "))
#      if age<12:
#         print("Pay $5")
#      elif (age>=12) and (age<=18):
#         print("Pay $7")
#      elif (age>=45) and (age<=55):
#         print("Have a free ride on us!!")
#      else: 
#         print("Pay $12")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
# 3.4
# weight= float(input("Enter Your Weight: "))
# height= float(input("Enter Your Height: "))
# BMI = round(weight/(height**2))
# if BMI<18.5:
#     print(f"Your bmi is {BMI},you are underweight")
# elif BMI<25:
#     print(f"Your bmi is {BMI},you have a normal weight")
# elif BMI<30:
#     print(f"Your bmi is {BMI},you are overweight")
# elif BMI<35:
#     print(f"Your bmi is {BMI},you are obese")
# else:
#     print(f"Your bmi is {BMI},you are clinically obese")
# 3.5
# leapYear = int(input("Enter a Year: "))
# if (leapYear%4==0):
#     if leapYear%100==0:
#         if leapYear%400==0:
#             print("This is a leap year")
#         else:
#             print("This is not a leap year")
#     else:
#         print("This is a leap year")
# else:
#     print("This is not a leap year")
# 3.6
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height(cm)? "))
# if height>=120:
#      print("You can ride the rollercoaster!")
#      age = int(input("Put your age for price "))
#      if age<12:
#         bill1=8
#         photos = input("Do You want click photo? y/n ")
#         if photos=='y':
#            print(f"Your total bill is ${bill1}")
#         if photos == 'n':
#            print("your total bill is $5")
#      elif (age>=12) and (age<=18):
#         bill2=10
#         photos = input("Do You want click photo? y/n ")
#         if photos=='y':
#            print(f"Your total bill is ${bill2}")
#         if photos == 'n':
#            print("your total bill $7")      
#      else: 
#         bill3=15;
#         photos = input("Do You want click photo? y/n ")
#         if photos=='y':
#            print(f"Your total bill is ${bill3}")
#         if photos == 'n':
#            print("your total bill is $12")
     
# else:
#     print("Sorry, you have to grow taller before you can ride.")
# another method
# bill=0
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height(cm)? "))
# if height>=120:
#      print("You can ride the rollercoaster!")
#      age = int(input("Put your age for price "))
#      if age<12:
#         bill=5
        
#      elif (age>=12) and (age<=18):
#         bill=10      
#      else: 
#         bill=15;
#      photos = input("Do You want click photo? y/n ")
#      if photos=='y':
#         bill_new=bill+3;
#         print(f"Your total bill is ${bill_new}")
#      if photos == 'n':
#          print(f"your total bill is ${bill}")
     
# else:
#     print("Sorry, you have to grow taller before you can ride.")
# 3.7
# s=0
# p=0
# l=0
# m=0
# ch=0
# pizza = input("Which type of pizza You want: ")
# pepperoni=input("Do you want to add pepperoni: ")
# extra_chesse = input("Do you want to add extra_Chesse: ")
# if pizza=='s':
#     s=15
#     if pepperoni=='y':
#         p=2 
#     if extra_chesse=='y':
#                ch=1
    
#     print(f"The total bill is {s+p+ch}")
# if pizza=='m':
#     m=20
#     if pepperoni=='y':
#         p=3 
#     if extra_chesse=='y':
#            ch=1
    
#     print(f"The total bill is {m+p+ch}")
# if pizza=='l':
#     l=25
#     if pepperoni=='y':
#         p=3 
#     if extra_chesse=='y':
#            ch=1
    
#     print(f"The total bill is {l+p+ch}")
# another method
# size = input("Which type of pizza You want: ")
# pepperoni=input("Do you want to add pepperoni: ")
# extra_chesse = input("Do you want to add extra_Chesse: ")
# bill = 0;
# if size =="S":
#     bill+=15
# elif size == "M":
#     bill+=20
# else:
#     bill+=25
# if pepperoni == "Y":
#     if size== "S":
#         bill+=2
#     else:
#         bill+=3
# if extra_chesse == "Y":
#     bill+= 1
# print(f"Your final bill is ${bill}")
# a = 9;
# if(a>10) and (a<13):
# if(a>10) or (a<13):
#     print("true");
# else:
#     print("false")
# 3.8
name1= input("Enter Your name? ")
name2= input("Enter her name? ")
name = name1 + name2
a = name.lower()
b1= a.count("t")
c1= a.count("r")
d1= a.count("u")
e1= a.count("e")
Total1= int(b1+c1+d1+e1)
b2= a.count("l")
c2= a.count("o")
d2= a.count("v")
e2= a.count("e")
Total2 = int(b2+c2+d2+e2)
score=(f"{Total1}{Total2}")
if (int(score)<10) or (int(score)>90):
    print("Your score is " + score+ ", You go together like coke and mentos")
elif (int(score)>=40) and (int(score)<=50):
    print("Your score is "+ score+", you are alright together")
else:
    print("Your score is "+ score)



 


   
