# Check given Name is present in list

name_list = ["Ali" , "Imran" , "Hammad" , "Khuram"]

name = input("Type your name: ")
if(name in name_list):
    print("This name is present in your list")
else:
    print("This name is out of list")