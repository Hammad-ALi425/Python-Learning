# Check the greatest of 4 numbers enter by user

a = int(input("Enter a 1st number: "))
b = int(input("Enter a 2nd number: "))
c = int(input("Enter a 3rd number: "))
d = int(input("Enter a 4th number: "))

if(a>b and a>c and a>d):
    print("1st number is greater")
elif (b>a and b>c and b>d):
    print("2nd number is greater")
elif (c>a and c>b and c>d):
    print("3rd number is greater")
else:
    print("4th number is greater")
