a=input("enter the number : ")
l=[int(i) for i in a]
print(l)
b=len(l)
lar=0
for i in range(0,b) :
    if l[i]>=lar :
        lar=l[i]
print(lar)   
c=l.index(lar)
print(c)   
flag=0
if l[0]!=l[-1] :
    flag=1
for i in range(0,c) :
    if l[i]>l[c] :
        flag=1
for i in range(c,b) :
    if l[c]<l[i] :
        flag=1
if flag==1 :
    print("entered number is not a hill number ")
else :
    print("entered number is a hill number ")                        
    

  



