def search(a,k):
    c=0
    index=[]
    for i in range(len(a)):
        if k==a[i]:
            c+=1
            index.append(i)
        else:
            continue
    return index

a=[10,20,10,70,80,30,10,50,30]
k=int(input("enter a no:"))
result=search(a,k)
if result:
    print("Item found at indices:",result)
else:
    print("Item not found")


