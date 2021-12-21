sub1 =int(input("Enter first Subject Marks\n: "))
sub2 =int(input("Enter Second Subject Marks\n: "))
sub3 =int(input("Enter Third Subject Marks\n: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("Your are Fail because you have less than 33% in one of the subjects")
    
elif(sub1+sub2+sub3)/3 < 40:
    print("You are Fail due to total percentage less than 40") 

else:
    print("Congrulation! You Have Passed the Exam")       
