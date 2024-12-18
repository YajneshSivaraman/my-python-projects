n=int(input("Enter a no:"))
for i in range(n+1):
    for j in range(i+1): #initailize range to 1 if you don't want  the program to execute from 0
        print(i,end=" ") #print j for type 2 number patter
    print("\n")

'''
Type 2 Number pattern
0 

0 1 

0 1 2 

0 1 2 3 
'''