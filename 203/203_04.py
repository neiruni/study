from decimal import *

ganpon = 100000
tuki = 20000
nenri = Decimal('0.07')
total = 0
buf = 0

for i in range(1,11,1):
    #年目
    year = str(i) + '年目'

    #通常
    total = ganpon + (tuki * 12 * i)

    #通常 × 年利
    if i ==1:
        buf = int(total + (total * nenri))
    else:
        buf = buf + tuki * 12
        a = (buf * nenri)
        buf = (buf + a).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
        

    print(year.rjust(10), ('{:,}'.format(total) + '円').rjust(10), ('{:,}'.format(buf) + '円').rjust(10))
    
