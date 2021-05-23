
class Hito():
    def __init__(self, name, weight, petname):
        self.name = name
        self.weight = weight
        self.petname = petname
    
    @staticmethod
    def name_get_func(self):
        return self.name

    def weight_get_func(self):
        return self.weight
    

class Pet(Hito):
    def __init__(self, petname, petweight):
        super().__init__(petname)
        self.petweight = petweight
        
    def name_get_func(self):
        return self.petname
    
    def name_set_func(self):
        buf = input()
        self.petname = buf
        return self.petname

    def weight_get_func(self):
        return self.petweight


hitoins = Hito('たろ', 100.3, 'たろたろ')
petins = Pet(petname='たろ', petweight=10.2)

print('飼い主：' + str(hitoins.name_get_func)  + 'kg ペット：' + str(petins.name_get_func) + ' ' + str(petins.weight_get_func) + 'kg')

