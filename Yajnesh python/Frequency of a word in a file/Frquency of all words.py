f=open("sample.txt","r")
d={}
for i in f.read().split():
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i,j in d.items():

    print(i,j)
