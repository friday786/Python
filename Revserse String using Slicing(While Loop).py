#Input string from user for revserse
string=str(input("Enter a String for Revserse Its: "))

#Define function
def reverse_Slice(string):
    return string[::-1]

print("The original string is: ",string)
print("Reverse string is: ",reverse_Slice(string))
