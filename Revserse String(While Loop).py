#Input string from user for revserse
string=str(input("Enter a String for Revserse Its: "))
#Print String
print("The Original String is:" ,string)
# Empty String
revser_String=""
# Find length of a string and save in count variable  
count=len(string)
#Use while loop for revserse string
while count>0:
    revser_String += string[count-1]  # save the value of str[count-1] in reverseString  
    count -= 1
print ("The reversed string is : ",revser_String)# reversed string 