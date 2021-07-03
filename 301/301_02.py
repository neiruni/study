
class usi:
    def __init__(self, name:str , nenrei:int , seibetu:bool, taizyu:int):
        usi.name = name
        usi.nenrei = nenrei
        usi.seibetu = seibetu
        usi.taizyu = taizyu
    
    def say(self):
        print(self.name, self.nenrei, self.seibetu, self.taizyu)


buf1 = usi('はなこ', '3歳',' メス', '100.4kg')
buf1.say()


buf2 = usi('たろう', '4歳',' オス', '200.5kg')
buf2.say()


buf3 = usi('むげん', '9歳',' オス', '300.6kg')
buf3.say()
