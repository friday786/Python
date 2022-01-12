n=3
for i in range(n):
    for j in range(n):
        if i!=1:
            print("*", end=" ")
    for j in range(n-1):
        if i == 1 :
            print("*",end="   ")
    print()