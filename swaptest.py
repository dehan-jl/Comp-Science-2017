def myswap(a, b):
    tmp = a
    a = b
    b = tmp
    p = [a, b]
    return p


x = 5
y = 10
p = myswap(x, y)
x = p[0]
y = p[1]
print("x", x)
print("y", y)