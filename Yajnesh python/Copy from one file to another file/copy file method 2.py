f1=input("Enter file to be copied")
f2=input("Enter destination file")
fread=open(f1,"r")
fwrite=open(f2,"w")
for line in fread.readlines():
    fwrite.write(line)
print("file is copied")
fread.close()
fwrite.close()



