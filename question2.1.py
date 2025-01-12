a=input("enter the string: ").lower()
ascii_values=[ord(char) for char in a]
print(ascii_values)
ascii_values.sort()
print(ascii_values)
b=[chr(value) for value in ascii_values]
print(b)
counted=set ()
for char in b :
    if char not in counted :
        c=b.count(char)
        print(f"the charcter {char} is reapted {c} times")
