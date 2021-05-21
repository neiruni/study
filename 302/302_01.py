
class Ningen():
    def __init__(self, ningenname, ningenweight):
        self.ningenname = ningenname
        self.ningenweight = ningenweight


class Kisyu():
    def __init__(self, kisyuname, kisyuweight):
        self.kisyuname = kisyuname
        self.kisyuweight = kisyuweight


class Uma():
    def __init__(self, umaname, umaweight, umaspeed):
        self.umaname = umaname
        self.umaweight = umaweight
        self.umaspeed = umaspeed

    #走るメソッド
    def run_func(self, *args):
        print(str(self.umaname) + '走る。(速度：' + str(self.umaspeed) + 'km/h）')

    #走る（騎手）メソッド
    def run_kisyu_func(self, *args):
        total = 0
        cnt = 0

        for i in args:
            total += i.kisyuweight
            cnt += 1
        
        if total <= 200:
            self.umaspeed = self.umaspeed - total / 20
            print(str(self.umaname) + '走る。乗馬者' + str(cnt) +'名(速度：' + str(self.umaspeed) + 'km/h）')
        else:
            exit()        

    #走る（人）メソッド
    def run_ningen_func(self, *args):
        total = 0
        cnt = 0

        for i in args:
            total += i.ningenweight
            cnt += 1
        
        if total <= 200:
            self.umaspeed = self.umaspeed - total / 10
            print(str(self.umaname) + '走る。乗馬者' + str(cnt) +'名(速度：' + str(self.umaspeed) + 'km/h）')
        else:
            exit()        
    

#馬インスタンス作成
umainsta = Uma('ディープインパクト', '200.5', 50)

#人インスタンス作成
Ningen1 = Ningen('人1', 80)

#騎手インスタンス作成
kisyu1 = Kisyu('たけゆたか', 50.2)
kisyu2 = Kisyu('たなか', 60.6)


print(umainsta.umaname + '（体重：' + str(umainsta.umaweight) + 'kg,速度：' + str(umainsta.umaspeed) + 'km/h')
print(kisyu1.kisyuname + '（体重：' + str(kisyu1.kisyuweight) + 'kg）')
print(kisyu2.kisyuname + '（体重：' + str(kisyu2.kisyuweight) + 'kg）')
print(Ningen1.ningenname + '（体重：' + str(Ningen1.ningenweight) + 'kg）')


umainsta.run_func()
#umainsta.run_kisyu_func(kisyu1.kisyuweight, kisyu2.kisyuweight)
umainsta.run_kisyu_func(kisyu1, kisyu2)
#umainsta.run_kisyu_func(Kisyu(), Kisyu())
#umainsta.run_kisyu_func(Kisyu('たけゆたか', 50.2), Kisyu('たなか', 60.6))
umainsta.run_ningen_func(Ningen1)












