
banana = 100
buy_banana = 25

momo = 300
buy_momo = 25

total = (banana * buy_banana) + (momo * buy_momo)

word = str(banana) + '円のバナナを' + str(buy_banana) + '個、' + str(momo) + '円の桃を' + str(buy_momo) + '個買ったら、合計' + '{:,}'.format(total) + '円になりました。'

print(word)
