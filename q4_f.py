f=open("q4_f.txt","r")
d=open("q4_delhi.txt","a")
s=open("q4_shimla.txt","a")
o=open("q4_others.txt","a")
for i in f:
    if f!="\n":
        if "delhi" in i:
            d.write(i)
            # d.write("\n")
        elif "shimla" in i:
            s.write(i)
            # s.write("\n")
        else:
            o.write(i)
            # o.write("\n")

f.close()
d.close()
s.close()
o.close()