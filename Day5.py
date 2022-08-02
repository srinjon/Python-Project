# 5.1
# fruits = ["Apple","Banana","Cherry"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit +" Pie")
# print(fruits)
# 5.2
# student_heights = input("Input a list of student height ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)
# no_of_students = 0
# for student in student_heights:
#     no_of_students +=1
# print(no_of_students)
# avg=str(round(total_height/len(student_heights)))
# print("avg: " + avg)
# ***********
# total = 0
# for i in range(0,len(student_heights)):
#     total = total + student_heights[i];
# print(total)
# Total=(sum(student_heights))
# print(Total/n)
# 5.3
# student_marks = input("Enter student marks: ").split()
# for n in range(0,len(student_marks)):
#     student_marks[n]=student_marks[n]
# print(student_marks)
# highest_marks=0
# for maximum in student_marks:
#     if int(maximum)>int(highest_marks):
#         highest_marks=maximum
# print(highest_marks)
# Or
# print(max(student_marks))
# 5.4
# num=0
# for number in range(1,101):
# # for number in range(1,101,3):
#     print(number)
#     num = num+number
# print(num)
# 5.5
# even = 0
# for number in range(2,101,2):
#     print(number)
#     even+=number
# print(even)
# another method
# total = 0
# for num in range(1,101):
#     if num % 2==0:
#         print(num)
#         total += num
# print(total)
# 5.6
for num in range(1,101):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
           print("Fizz")
    elif num%5==0:
         print("Buzz")
    else:
        print(num)
        
    
