from abc import ABCMeta, abstractmethod


class Controller(metaclass=ABCMeta):
    @abstractmethod
    def ButtonUp_func(self):
        pass

    @abstractmethod
    def ButtonDown_func(self):
        pass

    @abstractmethod
    def ButtonLeft_func(self):
        pass

    @abstractmethod
    def ButtonRight_func(self):
        pass


class Game():
    def __init__(self, title, character):
        self.title = title
        self.character = character
    
    def gamestart_func(self):
        print('{0}スタート'.format(self.title))
    
    
class Dorakoe(Controller, Game):
    def __init__(self, title, character):
        super().__init__(title, character)
        
    def ButtonUp_func(self):
        print(self.character + 'が上に進む')
    
    def ButtonDown_func(self):
        print(self.character + 'が下に進む')

    def ButtonLeft_func(self):
        print(self.character + 'が左に進む')

    def ButtonRight_func(self):
        print(self.character + 'が右に進む')


class Streatfaio(Controller, Game):
    def __init__(self, title, character):
        super().__init__(title, character)

    def ButtonUp_func(self):
        print(self.character + 'がジャンプする')
    
    def ButtonDown_func(self):
        print(self.character + 'がしゃがむ')

    def ButtonLeft_func(self):
        print(self.character + 'が後ろに進む')

    def ButtonRight_func(self):
        print(self.character + 'が前に進む')

Dorakoe1 = Dorakoe('ドラコエ', '勇者')
Dorakoe1.gamestart_func()
Dorakoe1.ButtonUp_func()
Dorakoe1.ButtonDown_func()
Dorakoe1.ButtonLeft_func()
Dorakoe1.ButtonRight_func()


Streatfaio1 = Streatfaio('ストリートフォイター', '春香')
Streatfaio1.gamestart_func()
Streatfaio1.ButtonUp_func()
Streatfaio1.ButtonDown_func()
Streatfaio1.ButtonLeft_func()
Streatfaio1.ButtonRight_func()
