from decimal import *


class Pikachu():

    def __init__(self, hitpoint, power, defense, speed):
        self.hitpoint = hitpoint
        self.power = power
        self.defense = defense
        self.speed = speed
        self.name = 'ピカチュウ'
    
    def denkousekka(self):
        waza = '電光石火'
        damage = self.power * Decimal('1.3')
        damage = damage.quantize(Decimal("0"), rounding=ROUND_HALF_UP)
        return waza ,damage

    def boruto(self):
        waza = '10万ボルト'
        damage = self.power * Decimal('1.3')
        damage = damage.quantize(Decimal("0"), rounding=ROUND_HALF_UP)
        return waza, damage

    def tail(self):
        waza = 'アイアンテール'
        damage = self.power * Decimal('1.3')
        damage = damage.quantize(Decimal("0"), rounding=ROUND_HALF_UP)
        return waza ,damage
    

class Raichu(Pikachu):
    
    def __init__(self, hitpoint, power, defense, speed):
        super().__init__(hitpoint, power, defense, speed)

        self.name = 'ライチュウ'
        self.power = self.power * 2
    
    def zutsuki(self):
        waza = 'ロケット頭突き'
        damage = self.power * Decimal('1.1')
        damage = damage.quantize(Decimal("0"), rounding=ROUND_HALF_UP)
        return waza ,damage
    
    def panti(self):
        waza = 'かみなりパンチ'
        damage = self.power * Decimal('1.1')
        damage = damage.quantize(Decimal("0"), rounding=ROUND_HALF_UP)
        return waza ,damage
    
    def kaminari(self):
        waza = 'かみなり'
        damage = self.power * Decimal('1.1')
        damage = damage.quantize(Decimal("0"), rounding=ROUND_HALF_UP)
        return waza ,damage
    

Pikachu = Pikachu(3000, 100, 200, 500)
Raichu = Raichu(3000, 100, 200, 500)


print('さとし' + Pikachu.name + 'が' + str(Pikachu.denkousekka()[0]) + 'をした。' + '（ダメージ：' +str(Pikachu.denkousekka()[1]) + '）')
print('さとし' + Pikachu.name + 'が' + str(Pikachu.boruto()[0]) + 'をした。' + '（ダメージ：' +str(Pikachu.boruto()[1]) + '）')

print('さとし' + Raichu.name + 'が' + str(Raichu.denkousekka()[0]) + 'をした。' + '（ダメージ：' +str(Raichu.denkousekka()[1]) + '）')
print('さとし' + Raichu.name + 'が' + str(Raichu.boruto()[0]) + 'をした。' + '（ダメージ：' +str(Raichu.boruto()[1]) + '）')
