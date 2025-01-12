a=input("enter the first string: ")
b=input("enter the second string : ")
c=len(a)
d=len(b)
flag=0
for i in range(0,c) :
    for j in range(0,d):
        if a[i]==b[j] :
            flag +=1
if flag==c :
    print("entered word is a anagram ")
else :
    print("entered word is not an anagram")               