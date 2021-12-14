letter= '''Dear <|name|>,
Greeeting from ABC coding House. I am happy to tell you about your selection,
You are Selected!
Hava a great day ahead!
Thanks for reagards
Bill     
Date : <|date|>    
'''
name=input("Enter a Name\n")
date=input("Enter Date\n")
letter=letter.replace("<|name|>", name)
letter=letter.replace("<|date|>", date)
print(letter)
 