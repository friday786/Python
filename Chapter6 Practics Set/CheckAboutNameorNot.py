text=input("Enter the Text: ")
if("Sir HARRY" in text):
    spam=True
elif("about harry" in text):
    spam=True
elif("Hi HaRRY" in text):
    spam=True
elif("Some one talk about harry" in text) :
    spam=True
else:
    spam=False
if(spam): 
    print("This string is talk about Harry")
else:
    print("This string is not talk about Harry")                   






