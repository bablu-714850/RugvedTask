a=input("enter the numbers :").split(" ")
l=[int(i) for i in a]
c=len(l)
for i in range (0,c) :
    pos=i
    for j in range (1,c) :
        if l[pos]>l[j] :
            pos=j
            l[i],l[pos]=l[pos],l[i]

print(f"the sorted list is {l}")
