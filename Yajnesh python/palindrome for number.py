#Method 1
print("METHOD 1")
a=(input("Enter No:"))
original=int(a)
d=0 #d is  the reversed digit
for i in range(len(a)):
    b=original%10
    d=(d*10)+b
    original=original//10
print(d)
if int(a)==d: #checks if the given input is same as reversed number(d)
    print("It is  a palindrome")
else:
    print("It is not a palindrome")

# ---------------------------
print("\n")
# ---------------------------

#Method 2
print("METHOD 2")
a=input("Enter no:")
b=a[::-1]
if a==b:
    print("It is  a palindrome")
else:
    print("It is not a palindrome")