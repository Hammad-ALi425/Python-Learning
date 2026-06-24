# Write a function to print element of a list in a single line

my_list = [45, 9, 78, 65, 7, 55]

def element(list):
    for i in list:
        print(i, end="\t")
element(my_list)