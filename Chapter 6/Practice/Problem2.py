# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

total_percent = (100*(marks1+marks2+marks3))/300

if(total_percent>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are pass ",total_percent)

else:
    print("You failed ",total_percent)