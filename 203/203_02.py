
total = 0
buf = 0 


for i in range(1,100,2):
    buf = total
    total = buf + i

    print(str(buf) + ' + ' + str(i) + ' = ' + str(total))

    