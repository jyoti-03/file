f=open("demo.txt","r")
c=0
for i in f:
    if f!="\n":
        c+=1
print(c)