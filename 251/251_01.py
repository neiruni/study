

class Player():
    def __init__(self, name, level, **kwargs):
        self.name = name
        self.level = level
        self.item_list = kwargs

    #playerの基本情報
    def player_info(self):
        print('Player Name：{}\nLevel：{}'.format(self.name, self.level))
    
    #Playerのitem情報
    def print_item_list(self):       
        cnt = 0 
        for keys in self.item_list.keys():
            item = self.item_list.get(keys, 'なし')
            self.items = Item(item[0], item[1])
            cnt += 1
            print('Item[{0}]：{1} × {2}'.format(cnt, self.items.name, self.items.count))
            
        # for item_name, item_count in self.item_list:
        #     self.items = Item(item_name, item_count)
        #     cnt += 1
        #     print('Item[{0}]：{1} × {2}'.format(cnt, self.items.name, self.items.count))


class Item():
    def __init__(self, name, count):
        self.name = name
        self.count = count


Player1 = Player('カリュプソー', 99, item1=('貝殻', 21), item2=('布団代わりのワカメ', 3), item3=('サングラス', 1), item4=('浮き輪', 1))
Player1.player_info()
Player1.print_item_list()


