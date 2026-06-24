# Write a recursive function to display Sum of first n natural number

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

s = sum(5)
print(s)

