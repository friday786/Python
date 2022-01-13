def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
a=int(input("Enter a Number: "))
b=sum(a)
print("Sum of First",a,"natural Number is",b)    