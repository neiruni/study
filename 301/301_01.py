import re

class keisan:
    def __init__(self, total, data):
        self.data = data
        self.total = total
 
    def tasu(self):
        self.total = int(self.total) + int(self.data)
        return self.total


total = 0
pattern ='[0-9]+'

while True:
    data = input('合計：' + str(total) + '\n')

    if re.fullmatch(pattern, data) is not None:
        a = keisan(total, data)
        total = a.tasu()
    else:
        print('終わります。')
        break
    

