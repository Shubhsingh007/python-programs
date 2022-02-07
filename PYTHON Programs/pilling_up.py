s=[1,2,1,3]
b=3
c=1
a=(max(s))
if (b or c )==a:
    print(a)
    s.remove(max(s))
    print(s[max])
    
    
    
    
    
    
    t=int(input())
a=int(input())
b=list(map(int,input().split()))
l=len(b)
for i in range(l):
    if b[i] == max(b):
       b.remove(max(b))
       print('y')
       print(max(b))
    elif b[l] == max(b):
       b.remove(max(b))
       print('y')