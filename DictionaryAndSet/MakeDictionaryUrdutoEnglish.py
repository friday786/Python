myDict={
    "Panka":"Fan",
    "Dabba":"Box",
    "Kapra":"Clothes",
    "Jota":"Shoes",
    "Mosam":"Season",
    "Sarde":"Cold"    
}
print("Option are ",myDict.keys())
a=input("Enter the Urdu Word\n ")
#Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is: ",myDict.get(a))
