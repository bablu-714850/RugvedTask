def credit(a):
    c=[]
    sum=0
    for i in range(0,len(a)) :

        if i%2==0 :
            d=2*a[i]

            if d>9 :
                d=d%10+int(d/10)
            c.append(d)
        else :
     
         c.append(a[i]) 
    print(c)    
    for i in range  (0,len(c)) :
        sum=sum+c[i]
    print(sum)    
    if sum%10==0 :
        print("credit card number is valid :")
    else :
         print("credit card number is not valid :")             



a=input("enter your credit card number : ")
l=[int(i) for i in a]
credit(l)
