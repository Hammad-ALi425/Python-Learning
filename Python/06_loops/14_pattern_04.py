# Print the following pattern
'''
For n=4

++++++
--  --
--  --
--  --
--  --
++++++

'''

n = int(input("Enter a number: "))
for i in range(1 , n+1):
    if(i==1 or i==n):
        print("+" * n)
    else:
        print("-" * 2 , end='')
        print(" " * (n-4), end='')
        print("-" * 2)