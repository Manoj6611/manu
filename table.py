size=int(input("enter the size of multiplication table"))
for i in range(1,size+1):
    for j in range(1,size+1):
     product=i*j
     print("{0:4}".format(product),end="")
    print()