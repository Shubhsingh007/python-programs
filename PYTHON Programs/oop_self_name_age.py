class PlayerCharacter:
  def __init__(self, name, age): 
    self.name = name 

    self.age = age 

  def run(self):

   print('run')

  def shubh(self):
    print(f'the age of the dog is{self.name}and he is {self.age}years')
    return 'done'
    
player1 = PlayerCharacter(' Cindy', 44)
player2=  PlayerCharacter('Tom', 21)


print(player1.shubh())

print(player2.age)