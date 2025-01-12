def letters(a):
    sum=0
    for i in range (0,len(a)) :
        if a[i]==" " or a[i]=="." :
            sum=sum+1
    b=len(a)-sum
    return b
def words(a) :
    sum=0
    for i in range (0,len(a)):
        if a[i]==" ":
            sum +=1
         
    return sum
def sentences(a):
    sum=0
    for i in range (0,len(a)) :
        if a[i]=="." :
            sum +=1
           
    return sum
def coleman(a) :
    l=letters(a)
    w=words(a)
    s=sentences(a)
    c=float((l/w)*100)
    d=float((s/w)*100)
    index= float(0.0588 * c - 0.0296 * d - 15.8)
    return index
        


a=input("enter the text : ")
print(f"the grade level of the given text is :{coleman(a)}")
print(letters(a))
print(words(a))
print(sentences(a))
