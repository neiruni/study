
n = 100

for i in range(1,n):

    keta = 10 ** (int(len(str(i)) -1))

    if len(str(i)) == 1:
        print(i, i)
    elif len(str(i)) > 1:
        q, mod = divmod(i, keta)
        total = mod * keta + q

        if i < total:
            print(i, total, 'ピコン！')
        else:
            print(i, total)

