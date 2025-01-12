c=['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encrypt(a,b) :
    cipher=""
    for char in a :
        e=c.index(char)
        f=e+b
        cipher+=c[f]
    print(f"the message after encrypt is {cipher}")        







a=input("enter the message that need to be encrypt : ")
b=int(input("enter the shift in numbers : "))
encrypt(a,b)