def CheckLeap(Year):
    if((Year % 400== 0) or
    (Year % 100 !=0)and
    (Year % 4 == 0)):
        print("Given Year is Leap Year");
    else:
         print("Given Year is not Leap Year");
Year=int(input("Enter The Number: "))
CheckLeap(Year)            