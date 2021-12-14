num=int(input("Enter a number to print Right Triangle Pattern: "))
print("Pattern print: ",num)
for i in range(num):
    for j in range(1,num-i):
        print(" ",end="")
    for k in range(0,i+1):
        print("*",end="")
    print()               
      