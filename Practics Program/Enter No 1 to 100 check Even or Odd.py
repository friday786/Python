num=int(input("Enter a Number: "))
if(num>50):
    if(num%2==0): #reminder in division with two for even numbers is always a zero.
        print("Even Number Multiply by 2: ",num*2)
    else:
       print("Odd Number Multiply by 3: ",num*3)
else:
    print("Number is less than 50 Multiply by 5: ",num*5)    
        