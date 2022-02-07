
# a list contains both even and odd numbers.  
seq = [0, 1, 2, 3, 5, 8, 13] 
  
# result contains odd numbers of the list 
result = filter(lambda x: x % 2 != 0, seq) 
print(list(result)) 
  
# result contains even numbers of the list 
result = filter(lambda x: x % 2 == 0, seq) 
print(list(result)) 

print(list(filter(lambda var:var*2,range(0,10))))#filter and give only is input as its output
print(list(map(lambda var:var*2,range(0,10))))