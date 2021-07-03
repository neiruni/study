
#親クラス
class sakana():
    def __init__(self, name):
        self.name = name

    def say(self):
        print(self.name + 'はすいすい泳ぐ')


class demekin(sakana):
    def __init__(self, name, move):
        super().__init__(name)
        self.move = move

    def say(self):
        print(self.name + 'は' + self.move + '泳いだ')
        

class same(sakana):
    def __init__(self, name, dousa):
        super().__init__(name)
        self.dousa = dousa

    def say(self):
        print(self.name + 'は' + self.dousa + '泳いだ')


class kuzira(sakana):
    def __init__(self, name, oyogi):
        super().__init__(name)
        self.oyogi = oyogi
    
    def say(self):
        print(self.name + 'は' + self.oyogi + '泳いだ')


obj = demekin('出目金', 'ふりふり')
obj.say()

obj = same('サメ', 'すいすい')
obj.say()

obj = kuzira('クジラ', 'ゆうがに')
obj.say()



