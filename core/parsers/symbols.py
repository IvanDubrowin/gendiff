
class Symbol:
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return self.label

    def __str__(self):
        return self.label


add = Symbol('+')
delete = Symbol('-')