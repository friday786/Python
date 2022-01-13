def table (num):  
 for i in range (1,11): 
  print (num, 'X', i ,'=' ,num*i)  
a = int(input("Enter the number : ")) 
table(a)

# Reverse Table using Function
def table (num):  
 for i in range (10,0,-1): 
  print (num, 'X', i ,'=' ,num*i)  
a = int(input("Enter the number : ")) 
table(a)