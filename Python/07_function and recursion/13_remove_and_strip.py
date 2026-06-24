# Write a function to remove a given word from a list and strip it at a same time


def remove(list , word):
    for item in list:
        list.remove(word)
        return list

list = ["Hammad" , "Ali" , "Hussnain" ,"in"]
print(remove(list , "in"))


my_list = []
def strip(my_list , word):
    for item in list:
        if not(item==word):
            my_list.append(item.strip(word))
        
    return my_list

print(strip(my_list , "in"))