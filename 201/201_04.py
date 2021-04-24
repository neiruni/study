
buf1 = 1.1
total = 0

for i in range(3):
    total += buf1
    
print(round(total,2))


total = 0

for i in range(3):
    if total == 0:
        total = buf1
    else:
        total *= buf1
    
print(round(total,4))

