f=open("sample.txt","r")
a=(f.read()).split()
n=input("Enter word:")
result=a.count(n)
print("Enter frequency of words:",result)