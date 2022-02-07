import re
from itertools import combinations
a=int(input())
b=input().split()
c=int(input())
ct=0
cd=0
d=list(combinations(b,c))
for i in d:
 s=''.join(i)
 cd=cd+1
 regex=re.compile('a')#whatever u will write in place of 'a' will be searched in next line
 if (regex.search(s)!=None):#if string 's' do no contain char'a' then ct+1
    ct=ct+1
print(ct/cd)
#example output
#4
#a a b c
#2

#output will be 0.75 as there will be 6 cases (a,a),(a,b),(a,c),(a,b),(a,c),(c,d)
#so only (c,d) cse dont contain a so it willl be 5/6 chances that is =0.8333(output) 