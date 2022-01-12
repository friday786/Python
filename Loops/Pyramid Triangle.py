num=int(input("Enter a Number for Pattern: "))
for i in range(num):
    print(" " * (num-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (num-i-1))
    
    
    