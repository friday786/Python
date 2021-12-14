nyc_bal=188
bal_pitt=247
total_distance=nyc_bal+bal_pitt
print(total_distance)
Calculator in Python
first=input("Enter First Number : ")
operator=input("Enter Operator (+,-,*,/,%,**) :")
second=input("Enter Second Number :")
first=int(first)
second=int(second)
if operator == "+":
     print(first+second)
elif operator == "-":
     print(first-second)    
elif operator == "*":
     print(first*second) 
elif operator == "/":
     print(first/second)     
elif operator == "%":
     print(first%second) 
elif operator == "**":
     print(first**second) 
      
#Calculate Time to travel
nyc_bal=188
bal_pitt=247
total_distance=nyc_bal+bal_pitt
print(total_distance)  
mph=65
time=total_distance/mph
print(time)
round(time,3)

