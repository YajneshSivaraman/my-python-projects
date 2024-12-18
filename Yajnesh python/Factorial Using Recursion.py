def fact(n):
    if n==0:
        return 1
    else:
        result=n*fact(n-1)
    return result
n=int(input("Enter number you wanna find factorial for:"))
print(fact(n))