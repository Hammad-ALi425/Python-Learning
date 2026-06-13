# Print Table of a number in reverse order

i = 10
num = int(input("Enter a number: "))
while(i>=1):
    print(num , "*" , i , "=" , num*i)
    i-=1  


print()

# Above program by for loop

n = int(input("Enter a number: "))
for i in range(10 , 0 ,-1):
    print(n , "*" , i , "=" , n*i)