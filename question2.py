a=input("enter the string: ")
ascii_values=[ord(char) for char in a]
print(ascii_values)
ascii_values.sort()
print(ascii_values)
b=[chr(value) for value in ascii_values]
print(b)
d=len(b)
for i in range(0,d) :
    c=b.count(b[i])
    print(f"the word {b[i]} is reapted {c} times")


    
           