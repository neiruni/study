
class Pikachu():

    def __init__(self, hitpoint, power, defense, speed):
        self.hitpoint = hitpoint
        self.power = power
        self.defense = defense
        self.speed = speed
    
    def waza(self):
        print('電光石火', '１０万ボルト', 'アイアンテール')
    
    def nakigoe(self):
        print('ピカチュウ！')


class Raichu(Pikachu):
    
    def __init__(self, hitpoint, power, defense, speed):
        super().__init__(hitpoint, power, defense, speed)

        self.hitpoint = self.hitpoint + 8000
        self.power = self.power * 2

    def sinkawaza(self):
        print('ロケット頭突き', 'かみなりパンチ', 'かみなり')
    
    def nakigoe(self):
        print('ラァーイ')



Pikachu = Pikachu(5000, 300, 400, 900)
Pikachu.nakigoe()

Raichu = Raichu(5000, 300, 400, 900)
print(Raichu.hitpoint, Raichu.power, Raichu.defense, Raichu.speed)

Raichu.waza()
Raichu.sinkawaza()
Raichu.nakigoe()