from decimal import *


class Pikachu():
    def __init__(self, user ,hitpoint, power, defense, speed):
        self.user = user
        self.hitpoint = hitpoint
        self.power = power
        self.defense = defense
        self.speed = speed
        self.name = 'ピカチュウ'
    
    def say(self, waza, damage):
        print('{0}{1}が{2}をした。（ダメージ：{3}）'.format(self.user, self.name, waza, damage))

    def denkousekka(self):
        waza = '電光石火'
        damage = int(self.power * 1.3)
        self.say(waza, damage)

    def boruto(self):
        waza = '10万ボルト'
        damage = int(self.power * 1.4)
        self.say(waza, damage)

    def tail(self):
        waza = 'アイアンテール'
        damage = int(self.power * 1.5)
        self.say(waza, damage)
    

class Raichu(Pikachu):
    def __init__(self, user, hitpoint, power, defense, speed):
        super().__init__(user, hitpoint, power, defense, speed)

        self.name = 'ライチュウ'
        self.power = self.power * 2
    
    def zutsuki(self):
        waza = 'ロケット頭突き'
        damage = int(self.power * 2.1)
        self.say(waza, damage)
    
    def panti(self):
        waza = 'かみなりパンチ'
        damage = int(self.power * 3.1)
        self.say(waza, damage)
    
    def kaminari(self):
        waza = 'かみなり'
        damage = int(self.power * 4.1)
        self.say(waza, damage)
    

    
Pikachu = Pikachu('さとし', 3000, 100, 200, 500)
Pikachu.denkousekka()
Pikachu.boruto()


Raichu = Raichu('ロケット団', 3000, 100, 200, 500)
Raichu.denkousekka()
Raichu.panti()

