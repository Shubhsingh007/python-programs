from random import randint

answer = randint(1, 10)
while True:
        print(answer)
        guess=int(input('enter a no 1-10  '))
        if 0< guess <11:
            if  guess == answer:
               print ('corrent choice')
               break
        
            else:
               print('whong choice')
