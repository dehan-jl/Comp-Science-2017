def myswap(list):
    tmp = list[0]
    list[0] = list[1]
    list[1] = tmp

list1 = ["a", "b"]
myswap(list1)
print(list1)