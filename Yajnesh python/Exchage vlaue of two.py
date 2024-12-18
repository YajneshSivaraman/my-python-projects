#using tuple assignment
a=int(input("Enter a no:"))
b=int(input("Enter another no:"))
print(a,b)
(a,b)=(b,a)
print("The changed order is:",a,b)
#---------------------------------
#Using third Variable
print("Method 2")
a=int(input("Enter a no:"))
b=int(input("Enter another no:"))
print(a,b)
t=a
a=b
b=t
print("The changed order is:",a,b)