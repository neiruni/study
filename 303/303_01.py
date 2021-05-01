
class Pikachu():

    def __init__(self, hitpoint, power, defense, speed):
        self.hitpoint = hitpoint
        self.power = power
        self.defense = defense
        self.speed = speed
    
    def waza(self):
        print('電光石火', '１０万ボルト', 'アイアンテール')
    
    def nakigoe(self, sound='ピカチュウ！'):
        print(sound)
        


class Raichu(Pikachu):
    
    def __init__(self, hitpoint, power, defense, speed):
        super().__init__(hitpoint, power, defense, speed)

        self.hitpoint = self.hitpoint + 8000
        self.power = self.power * 2

    def sinkawaza(self):
        print('ロケット頭突き', 'かみなりパンチ', 'かみなり')
    



buf = Pikachu(5000, 300, 400, 900)
buf.nakigoe()

buf = Raichu(5000, 300, 400, 900)
print(buf.hitpoint, buf.power, buf.defense, buf.speed)
buf.waza()
buf.sinkawaza()
buf.nakigoe('ラァーイ')