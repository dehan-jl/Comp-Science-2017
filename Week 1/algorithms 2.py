def validate(x, m):
    if x > m:
        return False
    elif x <= 0:
        return False
    else:
        return True

def getinput(m):
    vali = False
    while vali == False:
        n = int(input("Enter an int less than " + str(m) +": "))
        vali = validate(n, m)
        if vali == False:
        	print("Error")
    return n

def search():
    x = int(input("Input a number to search for: "))
    found = False
    for i in range(len(car)):
        if car[i][0] == x:
            found = True
            break
    if found == False:
        print("Could not find that number.")
    else:
        print("The number was at index", car[i][1])

def printdata():
    print("Value | Index")
    for i in range(len(car)):
        print(str(car[i][0]).rjust(3) + ' '*3 + '|', end='')
        print(str(car[i][1]).rjust(4))

def bubblesort():
    print("Sorting...")
    sortq = False
    swaps = 0
    while sortq == False:
        for i in range(len(car)-1):
            if car[i][0] > car[i+1][0]:
            	#Swap
                tmp = car[i]
                car[i] = car[i+1]
                car[i+1] = tmp
                swaps += 1
        if swaps == 0:
            sortq = True
        else:
            swaps = 0
            
def info():
	total = 0
	for i in range(len(car)):
		total += car[i][0]
	print("Avg:", total/len(car))
	print("Max:", car[len(car)-1][0])
	
#Main
car = []
B = getinput(10)

for i in range(B):
    C = getinput(100)
    t = [C, i + 1]
    car.append(t)

printdata()
bubblesort()
printdata()
info()
search()
