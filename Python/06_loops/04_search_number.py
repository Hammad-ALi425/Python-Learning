# Search for a number x using while loop
# (1,4,9,16,25,36,49,64,81,100)
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49
i = 0
while i<len(tup):
    if(tup[i]==x):
        print("Found at index" , i)
        break
    else:
        print("Finding...")
    i+=1



# Above Program by for Loop
num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 64)
x = 64
idx = 0

for elements in num:
    if(elements==x):
        print("Found at index" , idx+1)
        break
    idx+=1
