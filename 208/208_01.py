
try:
    f = open('input.txt', 'r', encoding='UTF-8')
    data = f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print('error')
