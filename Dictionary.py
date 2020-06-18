# program to create phonebook and check whether name input after is there or not if it exist then show its details and if not display message Not Found
n = int(input())
d = {}
for i in range(n):
    x = input().split()
    d[x[0]] = x[1]
while True:
    try:
        name = input()
        if name in d:
            print(name, "=", d[name], sep="")
        else : print("Not Found")   
    except: break
