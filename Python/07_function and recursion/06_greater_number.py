# Write a function to print Greatest of 3 numbers

def greater (a , b , c):
    if(a>b and a>c):
        return f"1st number is greater: {a}"
    elif(b>a and b>c):
        return f"2nd number is greater: {b}"
    else:
        return f"3rd number is greater: {c}"

grter = greater(784,4546,33544)
print(grter)