list=[int(x) for x in input("Enter a no separated by a space:").split()]
for i in range (len(list)):
    for j in range(i):
        if list[j]<list[i]: #change list[j]>list[i] (to find the minimum in a list)
            list[j]=list[i]
print(list)
print("The maximum value in list:",list[0])
