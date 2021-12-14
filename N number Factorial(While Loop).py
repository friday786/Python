# Take a number of input from the user
# Initialize a factorial variable to 1
# A while loop is used to multiply the number to find factorial (for the continuing process)
# This process continue until the value of the number is greater than zero
# The factorial of the given number is printed

#takes input from user
num=int(input("Enter a Number to find factorial: "))

factorail=1 #declare and initialize factorial variable to one

#check if the number is negetive ,positive or zero
if num<0:
    print("Factorial does not defined for negative number.")
elif(num==0):
    print("The Factorial of 0 and 1")    
else:
    while num>0:
        factorail*=num
        num-=1
    print("Factorial of given number is: "+str(factorail))
          
