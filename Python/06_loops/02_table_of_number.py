# Print Table of a number enter by user

i = 1
num = int(input("Enter the number for printing a table: "))
while i<=10:
    print(num , "*" , i , "=" , num*i)
    i+=1