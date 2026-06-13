# Detect the comment and show the given comment is spam or not.

com1 = "Hello bro"
com2 = "Click here"
com3 = "You can do it"
com4 = "Hey"

comment = input("Enter your string: ")
if(com1 in comment or com2 in comment or com3 in comment or com4 in comment ):
    print("Your comment is spam")
else:
    print("Your comment is not a spam")