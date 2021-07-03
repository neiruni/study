import dataclasses

#Itemクラス
@dataclasses.dataclass
class Item():
    item_name: str
    item_count: int
    item_dict = {}

    def set_name(self):
        if self.item_name not in self.item_dict:
            self.item_dict[self.item_name] = 0
  
    def get_names(self):
        item_name_list = []
        for item_name in self.item_dict.keys():
            item_name_list.append(item_name)
        return item_name_list

    def set_count(self):
        self.item_dict[self.item_name] = self.item_dict[self.item_name] + self.item_count
 
    def get_count(self):
        item_count_list = []
        for item_count in self.item_dict.values():
            item_count_list.append(item_count)
        return item_count_list


#Bagクラス
class Bag:
    def getitems(self, item_name, item_count):
        return Item(item_name, item_count)
    

#Playerクラス
class Player():
    def __init__(self):
        self.instance_bag = Bag()
        
    #アイテム追加
    def item_push(self, item_name, item_count):
        self.instance_bag.getitems(item_name, item_count).set_name()
        self.instance_bag.getitems(item_name, item_count).set_count()
        
    #アイテム取り出し
    def item_pop(self, item_name, item_count):
        item_name = self.instance_bag.getitems(item_name, item_count).get_names()
        item_count = self.instance_bag.getitems(item_name, item_count).get_count()

        print('持ち物')
        for i in range(len(item_name)):
            print('{0}：{1}こ'.format(item_name[i], item_count[i]))

    #アイテム使用
    def item_eat(self, item_name, item_count):
        print('Playerは{0}を{1}こ食べた'.format(item_name, item_count))

        item_count = -item_count
        self.instance_bag.getitems(item_name, item_count).set_name()
        self.instance_bag.getitems(item_name, item_count).set_count()
        

        


player1 = Player()
player1.item_push('リンゴ', 3)
player1.item_push('パン', 5)
player1.item_pop('',0)
player1.item_eat('リンゴ', 2)
player1.item_pop('',0)




