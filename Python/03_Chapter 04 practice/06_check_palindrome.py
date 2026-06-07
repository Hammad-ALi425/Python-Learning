# Check if list contains a palindrome of elements or not.

my_list = [1, "abc", "abc", 1]
new_list = my_list[::-1]            # It can reverse our list.
if (new_list==my_list):
    print("palindrome")
else:
    print("Not a Palindrome")

