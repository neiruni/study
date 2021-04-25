


buf1 = 0
buf2 = 0

for i in list1:
    for j in list1:
        if list1[i][j] == '〇':
            buf1 += 1 
        elif list1[i][j] == '●':
            buf2 += 1


if buf1 == buf2:
    print('引き分け')
elif buf1 > buf2:
    print('〇'の勝ち)
elif buf1 < buf2:
    print('●'の勝ち)



