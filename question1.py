def triple_and(a,b,c):
    return a and b and c
    
d =bool(int(input("enter a first parameter 1 for true and 0 for false  : ")))
e =bool(int(input("enter a second parameter 1 for true and 0 for false : ")))
f =bool(int(input("enter a third parameter 1 for true and 0 for false  : ")))

print(triple_and(d,e,f))
