# A Student requires total 40% and at least 33% in each subject to pass.
# Assume 3 subjects and take marks as input.


marks1 = int(input("Enetr your marks in English: "))
marks2 = int(input("Enetr your marks in Maths: "))
marks3 = int(input("Enetr your marks in Computer: "))

total_marks = 300
percentage = ((marks1 + marks2 + marks3) / total_marks ) * 100

if(percentage >= 40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You have pass" , percentage)
else:
    print("You have failed", percentage)