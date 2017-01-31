def validate(x, m):
    if (x > m):
        return False
    elif (x <= 0):
        return False
    else:
        return True

def search(list):
    x = int(input("Input a number to search for: "))
    found = False
    for i in range(len(list)):
        if (list[i] == x):
            found = True
            break
    if found == False:
        print("Could not find that number.")
    else:
        print("The number was at spot", i+1)

A = 42
A += 10
vali = False
car = []

if (A > 40):
    while (vali == False):
        B = int(input("Enter an int less than 10: "))
        vali = validate(B, 10)

vali = False

for i in range(B):
    while (vali == False):
        C = int(input("Enter an int less than 100: "))
        vali = validate(C, 100)
    car.append(C)
    vali = False

print("Average:", sum(car)/B, "Max:", max(car))
search(car)