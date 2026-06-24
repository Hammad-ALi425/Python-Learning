# Write a recursive Function to print all elements of a list

def elements(list , idx=0):
    if idx==len(list):
        return
    print(list[idx])
    elements(list , idx+1)

items = ["Paper", "Wood", "Perfume", "Oil"]
elements(items)