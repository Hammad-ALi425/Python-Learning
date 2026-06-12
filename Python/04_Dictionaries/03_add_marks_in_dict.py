# Enter Marks of three subjects from user and store tem in dictionary. Use subject name as key and marks as value.

marks = {}      # At first we can store an empty dictionary

m1 = int (input("Marks of Maths: "))
marks.update({"Maths" : m1})            # It can add the marks of 1st subjects

m2 = int (input("Marks of Physics: "))
marks.update({"Physics" : m2})          # It can add the marks of 2nd subjects

m3 = int (input("Marks of English: "))
marks.update({"English" : m3})          # It can add the marks of 3rd subjects



print(marks)         # It can print the updated Dictionary

