import math
a=float(input("Enter the Length of Side a: "))
b=float(input("Enter the Length of Side b: "))
c=float(input("Enter the Length of Side c: "))

s=(a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(" Area of Triangle is: ",area)