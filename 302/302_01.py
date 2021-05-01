

class animal():
    def __init__(self, name):
        self.name = name


    def sound(self, motion='ワンワンと吠える'):
        print(self.name + 'が' + motion)


buf = animal('犬')
buf.sound()

buf = animal('魚')
buf.sound('すいすい泳ぐ')

