def rotate(s,g):
    temps = ''
    length = len(s)
    i = 0
    while i < length:
        startindex = s[0]
        temps = s[1:]
        temps = temps + startindex
        s = temps
        print(temps)
        if temps == goal:
            return True
        i += 1
    if temps != goal:
        return False

string = input("Enter String: ")
goal = input("Enter Goal: ")
res = rotate(string,goal)
print(res)
