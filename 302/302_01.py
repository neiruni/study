
class Human():
    def __init__(self, name, weight):
        self.name = name        
        self.weight = weight

    def info_func(self):
        print('{0}（体重：{1}kg）'.format(self.name, self.weight))


class Kisyu():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def info_func(self):
        print('{0}（体重：{1}kg）'.format(self.name, self.weight))


class House():
    def __init__(self, name, weight, speed):
        self.name = name
        self.weight = weight
        self.speed = speed
    
    def info_func(self):
        print('{0}（体重：{1}kg,速度{2}km/h）'.format(self.name, self.weight, self.speed))
    
    def say_func(self, name, speed):
        print('{0}走る。(速度：{1}km/h）'.format(name, speed))
    
    def say_2_func(self, name, cnt, speed):
        print('{0}走る。乗馬者{1}名(速度：{2}km/h）'.format(name, cnt, speed))

    #走るメソッド
    def run_func(self, *args):
        weight_total = 0
        cnt = 0

        if len(args) == 0:
            self.say_func(self.name, self.speed)
        else:
            for obj in args:
                weight_total += obj.weight
                cnt += 1

            if isinstance(obj, Kisyu):
                self.speed = self.speed - weight_total / 20
            elif isinstance(obj, Human):
                self.speed = self.speed - weight_total / 10
            
            self.say_2_func(self.name, cnt, self.speed)


#馬インスタンス作成
umainsta = House('ディープインパクト', '200.5', 50)
umainsta.info_func()

#人インスタンス作成
human1 = Human('人1', 80)
human1.info_func()

#騎手インスタンス作成
kisyu1 = Kisyu('たけゆたか', 50.2)
kisyu1.info_func()

kisyu2 = Kisyu('たなか', 60.6)
kisyu2.info_func()

umainsta.run_func()
umainsta.run_func(human1)
umainsta.run_func(kisyu1, kisyu2)













