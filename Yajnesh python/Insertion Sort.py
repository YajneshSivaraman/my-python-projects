a=[int(x) for x in input("Enter numbers seperated by a space:").split()]
for i in range(len(a)):
    k=a[i]
    j=i-1
    while j>=0 and k<a[j]:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=k
print("Sorted list:",a)