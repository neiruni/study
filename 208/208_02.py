
list1 =[]
buf = ''

while buf != 'exit':
    buf = input()
    if buf != 'exit':
        list1.append(buf)


try:
    f = open('input.txt', 'w', encoding='UTF-8')
    
    for i in list1:
        f.write(i + '\n')

    f.close()
except FileNotFoundError:
    print('error')


