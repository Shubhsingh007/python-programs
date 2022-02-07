s=input()
a=''
b=''
c=''
d=''
f=[]
g=''
j=[]
k=''
l=''
for i in s:
    if i.islower():
        a=a+i
        d=list(sorted(a))
      
    elif i.isupper():
        b=b+i
        l=list(b)
        l.sort()
        
    elif i.isnumeric() :     
       if int(i)%2==0:
         k=k+str(i)
         f=list(k)
         f.sort()
         
 
       elif int(i)%2!=0:
         g=g+str(i)
         j=list(g)
         j.sort()
print(''.join(d),end='')
print(''.join(l),end='')
print(''.join(j),end='')
print(''.join(f))