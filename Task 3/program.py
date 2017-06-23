def get_uname():
    correct = False
    while not correct:
        uname = input("Enter Username:")
        if checkvalid(uname):
            print("Correct Format")
            correct = True
        else:
            print("Incorrect Format")
    return uname

def checkchar(char, mn, mx):
    if mn <= ord(char) <= mx:
        return True
    else:
        return False

def checkvalid(uname):
    if len(username) != 6:
        return False
    if not checkchar(uname[0], 65, 90):
        return False
    if not checkchar(uname[1], 97, 122):
        return False
    if not checkchar(uname[2], 97, 122):
        return False
    try:
        int(username[3:])
    except:
        return False
    return True

def get_data(file):
    n = int(input("How many members:"))
    for i in range(n):
        name = input("Enter Name:")
        uname = input("Enter Username:")
        file.write(name + "," + uname + "\n")

def create():
    file = open("members.csv", "w")
    get_data(file)
    file.close()


def display():
    file = open("members.csv", "r")
    print("Name:".ljust(8), "|", "Username:".ljust(8))
    for line in file:
        l = line.rstrip()
        c = l.find(",")
        print((l[:c]).ljust(8), "|", (l[c + 1:]).ljust(8))
    file.close()

def find():
    file = open("members.csv", "r")
    query = input("Search query:")
    found = False
    for line in file:
        l = line.rstrip()
        c = l.find(",")
        if (l[:c]).lower() == query.lower():
            print("Name found, username is:", (l[c + 1:]))
            found = True
            break
    if not found:
        print("Name not found")
    file.close()

def append():
    file = open("members.csv", "a")
    get_data(file)
    file.close()


create()
display()
find()
append()
display()

