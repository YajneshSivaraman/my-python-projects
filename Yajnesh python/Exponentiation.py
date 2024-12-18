#METHOD 1
print("Method 1")
n=int(input("Enter number:"))
e=int(input("Enter exponent:"))
result=n**e
print("Result:",result)
#---------------------------
#METHOD 2
print("Method 2")
n=int(input("Enter number:"))
e=int(input("Enter exponent:"))
result=1
for i in range(e):
    result=result*n
print(result)