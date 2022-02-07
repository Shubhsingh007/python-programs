from itertools import permutations
s,i = input().split()
i = int(i)

s = list(s)

s.sort()
for per in list(permutations(s,i)):
    print(''.join(per))
