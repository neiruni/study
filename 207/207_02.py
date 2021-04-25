
def keisan(power, magic, charm):
    buf = ((power * 1.5) + (magic * 1.7)) * (charm / 10)
    return buf

dict1 = {
    'ヨシヒコ':[70, 30, 50],
    'ダンジョ':[90, 0, 45],
    'ムラサキ':[10, 80, 90],
    'メレブ':[20, 50, 5],
    }


for key, value in dict1.items():
    buf1 = value[0]
    buf2 = value[1]
    buf3 = value[2]

    total = keisan(buf1, buf2, buf3)
    
    print(key + '：', total)
