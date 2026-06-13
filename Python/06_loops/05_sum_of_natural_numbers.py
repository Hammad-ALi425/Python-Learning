# Print Sum of first n natural numbers

i = 1
sum = 0
n = int(input("Type a number: "))
while(i<=n):
    sum += i
    i+=1
print("Sum of 1st n natural numbers is" , sum)


# By for loop

sum = 0
num = int(input("Type a number: "))
for i in range(1 , num+1):
    sum += i

print("Sum of 1st n natural numbers is" , sum)