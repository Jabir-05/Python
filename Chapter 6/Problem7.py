# 7. Write a program to find out whether a given post is talking about "Jabir" or not.


# post = "Hey jabir is  good and Jabir is very good and Jbr is great"

post = input("Enter the post: ")

if("Jabir".lower() in post.lower()):
    print("This post is talking about Jabir : ")


else:
    print("This post is not talking about Jabir :")
