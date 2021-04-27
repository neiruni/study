from bible import Bible
import string
import re



#検索単語の入力
buf = input('探したい単語を入力:')


#ファイル読込
try:
    text = Bible.read()
except FileNotFoundError():
    print('error')
    exit()


#行単位での読込
arry = text.readlines()
dic = {}
pattren = "[0-9]+"


#単語を辞書に登録
for row in arry:
    #lis = row.split()
    lis = re.split(' |\n|\'|-', row)

    for item in lis:
        item = item.translate(str.maketrans( '', '',string.punctuation))
            
        flag = re.fullmatch(pattren, item)

        if flag is None and item != '':
            if item in dic.keys():
                dic[item] = dic[item] + 1
            else:
                dic[item] = 1


#結果表示
if buf in dic.keys():
    print(str(buf) + 'は' + str(dic[buf]) + '回')
else:
    print('その単語はありません。')



#ランキング表示
buf = input('単語出現ランキングの表示順位を入力：')

dic = sorted(dic.items(), key = lambda x : x[1], reverse=True)

if re.fullmatch(pattren, buf) is not None:
    for i in range(int(buf)):
        data = dic[i]
        print((str(i+1) + '位').rjust(10), data[0].rjust(10), (str(data[1]) + '回').rjust(10))
else:
    print('ランキングは半角数字で入力してください。')


