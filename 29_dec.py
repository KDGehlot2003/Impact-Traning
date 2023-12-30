#int
a = 10
print(a)
print(type(a))
id(a)

#float
a = 12.5
print(a)
print(type(a))

#str
s = "kiran"
print(s)
print(type(s))

#bool
s = "Rohit Sharma"
print(s)
b = bool(s)
print(b)

s = 5<2
print(s)
d = 4>1
print(d)
type(d)

#complex
s = 3 + 4j
print(s.real)
print(s.imag)
# s.real = 10           Readonly Attribute


# taking multiple input in oneline usinf map function
a,b = map(int,input("Enter values:").split(","))
print(a)
print(b)
