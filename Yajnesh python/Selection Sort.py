a=[int(x) for x in input("Enter numbers seperated by a space:").split()]
for i in range(len(a)):
    for j in range(i):
        if a[i]<a[j]:
            (a[j],a[i])=(a[i],a[j])
print("Sorted list:",a)