from decimal import Decimal

buf1 = Decimal('1.1')

total = 0
for i in range(3):
    total += buf1
    
print(total)


total = 0
for i in range(3):
    if total == 0:
        total = buf1
    else:
        total *= buf1
    
print(total)

