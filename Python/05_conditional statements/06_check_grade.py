# Check the grade According to followin scheme:
# 90-100 = A+
# 80-89  = A
# 70-79  = B
# 60-69  = C
# 50-59  = D
# <50    = F

marks = int(input("Enter your marks: "))

if(marks>=90 ):
    print("Your Grade is:")
    print("A+")
elif(marks>=80):
    print("Your Grade is:")
    print("A")
elif(marks>=70):
    print("Your Grade is:")
    print("B")
elif(marks>=60):
    print("Your Grade is:")
    print("C")
elif(marks>=50):
    print("Your Grade is:")
    print("D")
else:
    print("Your Grade is:")
    print("F")