
class mise:
    def __init__(self, data):
        self.zaiko = data
    
    def hiki(self):
        self.zaiko = self.zaiko - 1
        return self.zaiko

zaiko = 10

while True:

    print('在庫' + str(zaiko))
    buf = input()
    a = mise(zaiko)
    a = a.hiki()
    
    