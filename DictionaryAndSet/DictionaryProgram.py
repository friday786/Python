myDict={
    "Fast": "In a Quick Manner",
    "Qasim":"A Coder",
    "Harry":"Teacher",
    "Marks":[1,2,3],
    1:2
}
#print(myDict['Qasim'])

#Dictionary Method
#Key method gives key name
#print(myDict.keys())

#Dictionary type check
#print(type(myDict.keys()))


#print(list((myDict.keys())))#Print the Keys of dictionary
#print(myDict.values())#Print the Keys values of dictionary
#print(myDict.items())#Print the (key,values) for all items of dictionary

#update Dictionary
print(myDict)
updateDic={
    "Loviesh":"Friend",
    "Sobia":"Cute",
    "Jarvis":"Just a rather than very intelligent System",
    "Harry":"Good Teacher",
}
myDict.update(updateDic) #update the dictionary by adding key values pairs from updateDic
print(myDict)

# Get Method does not throw error
#but Single print throw an error if any value is not present in dictionary
print(myDict.get("Qasim2"))

