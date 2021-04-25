
list1 = [
    ['〇', '〇', '〇', '〇', '〇',],
    ['', '','●', '〇', '',],
    ['', '●', '〇', '●', '●',],
    ['', '●', '', '●', '',],
    ['', '', '', '', '●',],
    ]

buf1 = 0
buf2 = 0

for i in list1:
    for j in i:
        if j == '〇':
            buf1 += 1 
        elif j == '●':
            buf2 += 1


if buf1 == buf2:
    print('〇:' + str(buf1) + '個\n', '●:' + str(buf2) + '個\n', '引き分け')
elif buf1 > buf2:
    print('〇:' + str(buf1) + '個\n', '●:' + str(buf2) + '個\n', '〇の勝ち')
elif buf1 < buf2:
    print('〇:' + str(buf1) + '個\n', '●:' + str(buf2) + '個\n', '●の勝ち')


