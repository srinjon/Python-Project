print("Welcome to the tip calculator");
bill_amount = float(input("What was the total bill? $"))
tip_per = int(input("What percentage tip would you like to give? 10,12, or 15? "))
people = int(input("How many people to split the bill? "))
bill = bill_amount+((bill_amount*tip_per)/100)
total =(round((bill/people),2))
print(f"Each person should pay: ${total}")
