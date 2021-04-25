buf = input('なにを飲みますか？1：コーラ 2：ポーション\n')


def genkan():
    buf1 = ['【玄関に向かう】', '立ち上がる', '廊下を歩く', '扉を開ける', '']
    return buf1

def buy(data):
    if data == '1':
        buf2 = ['【買いに行く】', '道を歩く', 'お金を入れる', '飲み物を選択する', '']
    else:
        buf2 = ['【買いに行く】', '自転車に乗る', 'コンビニに向く', '自転車を走らせる', 'コンビニに入る', '飲み物を選択する', 'レジに向かう', 'お金を払う', '']
    
    return buf2

def modoru(data):
    if data == '1':
        buf3 = ['【戻る】', '道を歩く', '扉を開ける', '廊下を歩く', '']
    else:
        buf3 = ['【戻る】', '自転車に乗る', '自宅に向く', '自転車を走らせる', '扉を開ける', '廊下を歩く', '']
    return buf3

def nomu():
    buf4 = ['【飲む】', '栓を開ける', '飲む', '']
    return buf4


a = genkan()
b = buy(buf)
c = modoru(buf)
d = nomu()

for i  in a:
    print(i)

for i in b:
    print(i)

for i in c:
    print(i)

for i in d:
    print(i)
