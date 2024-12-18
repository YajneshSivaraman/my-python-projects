print("Mark Statement")
b=[]
c=0
b.append(int(input("Enter your Math mark:")))
b.append(int(input("Enter your English mark:")))
b.append(int(input("Enter your Python mark:")))
b.append(int(input("Enter your Physics mark")))
d=len(b)
for i in b:
    if i>=50:
        c+=1
    else:
        continue
total=0
if c==4:
    for i in b:
        total+=i
    percent=round((total/400)*100)
    print("You have passed all subject")
    print("Your total percentage is:",percent)
else:
    print("You have failed in",d-c,"subjects")
    for i in b:
        total+=i
    percent=round((total/400)*100)
    print("Your total percentage is:", percent,"%")


