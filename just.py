l=[24.2,21,11.5,51,[34,6,8,11]]
i=0
sum=0
while i<len(l):
    if type(l[i]) == list:
        ii=0
        while ii<len(l[i]):
            sum+=l[i][ii]
            ii+=1
    i+=1
print(sum)