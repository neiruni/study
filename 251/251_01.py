
class item():
    def __init__(self, name, count):
        self.name = name
        self.count = count


class player():
    def __init__(self, name, level, items):
        self.name = name
        self.level = level
        self.items = item()

