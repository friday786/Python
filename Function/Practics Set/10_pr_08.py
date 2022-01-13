def remove_and_split(string,word):
    newStr=string.replace(word,"")
    return newStr.strip()
    
this="       Qasim is Great Programmer      "
n=remove_and_split(this,"Qasim")
print(n)    