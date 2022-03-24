bl=["Kotak","HDFC","RBL","SBI","Bank of Baroda"]
f = open("q3_f.txt", "a")
i=0
while i<len(bl):
    f.write(bl[i])
    f.write("\n")
    i+=1
