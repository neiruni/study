import re

class mise:
    def __init__(self, name, stock, total):
        self.name = name
        self.stock = stock
        self.total = total
    
    def hiku(self):
        self.stock = int(self.stock) - 1
        return self.stock
    
    def goukei(self):
        self.total = int(self.total) + 1
        return self.total

stock = 10
Atotal = 0
Btotal = 0
Ctotal = 0
pattern = '[A-C]+'


n = 3
a = ["paiza"] * n
print(a)

while True:
    buf = input('A：大阪店 B：名古屋店 C：北海道店\n')
    
    if re.fullmatch(pattern, buf) is not None:
        if buf == 'A':
            A = mise(buf, stock, Atotal)  
            stock = A.hiku()  
            Atotal = A.goukei()
        elif buf == 'B':
            B = mise(buf, stock, Btotal)
            stock = B.hiku()  
            Btotal = B.goukei()
        elif buf == 'C':
            C = mise(buf, stock, Ctotal)
            stock = C.hiku() 
            Ctotal = C.goukei() 
        
       
        if stock != 0:
            print('在庫' + str(stock))
        else:
            print('在庫切れ、閉店です。')
            exit()
    else:
        print('存在しない店舗です。')
        exit()


