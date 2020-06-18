# program to create phonebook and check whether name input after is there or not if it exist then show its details and if not display message Not Found
n = int(input())
d = {}
for i in range(n):
    x = input().split()              # give inputs in two part and then click enter and give next inputs in two parts
    d[x[0]] = x[1]                    # here we are mapping the value of 2nd input in side first input(i.e assigning phone to thier respective names
while True:
    try:
        name = input()
        if name in d:
            print(name, "=", d[name], sep="")
        else : print("Not Found")   
    except: break
