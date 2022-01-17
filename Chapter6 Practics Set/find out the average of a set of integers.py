count=int(input("Enter the count of Number: "))

i=0
sum=0
for i in range(count):
    x=int(input("Enter the Integer: "))
    sum+=x
avg=sum/count
print(" Average of Number is: ",avg)    