print ('Hello World')

i = 1 
str = "*"
while i <= 9:
    print( str)
    i = i + 1
    str += "*"


i = 1 
str2 = str
while i <= 9:
    str2 = str2[:-1]
    print(str2)
    i = i + 1
    
    

print ("===")