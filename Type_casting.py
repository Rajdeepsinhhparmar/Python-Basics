x = 1
y = 2.5
z = "3"

y = int(y)
z = int(z)
x , y , z = float(x) , float(y), float(z)


print(x)
print(y)
print(z*2)
print(type(x))
print(type(y))
print(type(z))

x , y , z = str(x), str(y), str(z)

print("X is "+x)
print("Y is "+y)
print("Z is "+z*2)