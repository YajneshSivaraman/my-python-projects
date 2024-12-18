def newt(n,accuracy):
    x=n
    while True:
        root = 0.5*(x+(n/x))
        if (abs(root-x)<accuracy):
            return(root)
        print(root)
        x=root
n=float(input("Enter a no:"))
accuracy=float(input("Enter accuracy:"))
print(newt(n,accuracy))