# justify 

text = "banana"

#ljust()
# Take two paramenter length, character (only one character it takes)
# includes length of the text also 
# put space on the right side of string
# it return new tring 

print(text.ljust(20),"DATA") 
print(text.ljust(20, "o")) # len - 20 bananaoooooooooooooo 


# rjust()
# Take two paramenter length, character (only one character it takes)
# includes length of the text also 
# put space on the left side of string
# it return new tring 

print(text.rjust(20),"DATA") 
print(text.rjust(20,"o")) # len - 20 oooooooooooooobanana



# center()
# Take two paramenter length, character (only one character it takes)
# puts the text in the center 
# it return new tring 

print(text.center(20)) 
print(text.center(20,"-"))  # length will be 20 


# zfill() 
# add zeor at the begining of the string 
# it take one parameter as length( required )
# if values is greater than length no filling
# it return new tring 

myText = "50"

print(myText.zfill(10))

myText2 = "My name is prafull"

print(myText2.zfill(10))