print("~~~~~~~~~ Student Marksheet ~~~~~~~~~")
name = input("Enter the name of student: ")
rollno = int(input("Enter roll no: "))

Sub1 = int(input("Enter the marks of Python: ")) 
Sub2 = int(input("Enter the marks of DCN: ")) 
Sub3 = int(input("Enter the marks of SFDA: ")) 
Sub4 = int(input("Enter the marks of Linux: "))
Sub5 = int(input("Enter the marks of RM: "))

total = Sub1 + Sub2 + Sub3 + Sub4 + Sub5 
percentage = total/5

if percentage >= 50:
 print("Result is pass") 
else:
 print("Result is Fail")

print("Sub1",Sub1)
print("Sub2",Sub2)
print("Sub3",Sub3)
print("Sub4",Sub4)
print("Sub5",Sub5)

print("total: ",total)
print("percentage: ",percentage)
