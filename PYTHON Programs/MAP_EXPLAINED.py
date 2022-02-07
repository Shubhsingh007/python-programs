# List of strings 
l = ['sat', 'bat', 'cat', 'mat'] 
  
# map() can listify the list of strings individually 
test = list(filter(list, l)) 
print(test) 


#%%
# Python program to demonstrate working 
# of map. 
  
# Return double of n 
def addition(n): 
    return n + n 
  
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = filter(addition, numbers) #AK ak kar la list ko def function ma dala ga
print(list(result))