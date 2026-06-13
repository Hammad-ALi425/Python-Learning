# Check username is 10 characters long or not

username = input("Enter your name: ")

if(len(username) == 10):
    print("Length of username is 10")
elif(len(username)<10):
    print("Length of username is less than 10")
else:
    print("Length of username is greater than 10")

