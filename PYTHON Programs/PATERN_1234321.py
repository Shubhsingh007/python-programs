s=int(input())

for i in range(1,s+1):
    for j in range(1,i):
       print(j,end='')

    for j in range(i,0,-1):
      print(j,end='')
    print('')

