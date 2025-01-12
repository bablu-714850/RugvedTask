a=input("enter the string : ")
b=int(input("enter the number of divisions: "))
s=''
for i in range(1,len(a)) :
    if len(a)%b==0 :
        
        c=a[b*(i-1):b*i]
        s=s+c+"  "
    else :
        s='appropriate error'
print(s)            
