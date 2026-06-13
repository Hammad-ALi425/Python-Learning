# Print Factorial of a number by while loop

fact = 1
i = 1
n = int(input("Enter a number: "))
while(i<=n):
    fact = fact*i
    i+=1

print(fact)




# Print Factorial of a number by for loop

factorial = 1
num = int(input("Enter a number: "))

for i in range(1 , num+1):
    factorial = factorial*i

print(factorial)

