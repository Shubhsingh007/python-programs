def listToString(s): 

    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s)) 
        
        
# Driver code     
s = ['Geeks', 'for', 'Geeks'] 
print(listToString(s)) 







# Python program to convert a list 
# to string using list comprehension 

s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas'] 

# using list comprehension 
listToStr = ' '.join(map(str, s)) 

print(listToStr) 
