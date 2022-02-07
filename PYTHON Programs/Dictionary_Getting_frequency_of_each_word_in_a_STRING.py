d={}
f=int(input())
r=list(input().split())
for i in r:
    if i in d:
        d[i]+=1#if a char is already there in dictnry then add +1 every time to gets its ferq
    else:
        d[i]=1#else store 1 
print(dict(d))#print the dictionary 
#outputs give input =4
#12 312 12 124 12 4 24 1 4 124 233 
# output will be ={'12': 3, '312': 1, '124': 2, '4': 2, '24': 1, '1': 1, '233': 1}


d={}
f=int(input())
r=list(input().split())
for i in r:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for key, val in d.items():#storing keys and value from dictionary
        print(key,val)
#outputs give input =4
#1 2 3 
#output
# 1 1
# 2 1
# 3 1
 