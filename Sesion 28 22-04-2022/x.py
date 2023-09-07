for i in range(19+1):
    for c in range(19-i):
        print (" ",end="")
    for d in range(2*i-1):
        print("*",end="")
    print()
for i in range(19-1,0,-1):
    for c in range(19-i):
        print (" ",end="")
    for d in range(2*i-1):
        print("*", end="")
    print()