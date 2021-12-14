Number=int(input("Enter a Number to check Prime or Composite :"))
count = 0;
i=1
while(Number>=i):
    if(Number%i==0):
        count+=1;
    i+=1;
if(count > 2):
       print("%d is a composite number" % Number)
else:
   print("%d is a prime number" % Number)    


        