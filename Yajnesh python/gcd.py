def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=int(input("enter a no:"))
b=int(input("enter a no:"))
print(gcd(a,b))