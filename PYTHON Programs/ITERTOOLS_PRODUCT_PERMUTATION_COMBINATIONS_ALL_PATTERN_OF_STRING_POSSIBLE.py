from itertools import product,permutations,combinations
a=[1,2,3,4]
b=[5,6,7,8]
c=list(product(a,b))#give all possibe outcomes
d=list(permutations(a))#can alse write as (a,2),will consider (1,2) and (2,1) different
e=list(combinations(a,3))#cant be used as (a),wil consider (1,2) and (2,1) same so wn't inclde
print(c)
print(d)
print(e)
