class AST:
    def __init__(self, loader):
        self.data = loader.load()

    def switch(self, key, first, second):
        if self.is_nested(first.get(key), second.get(key)):
            child = self.parse(first.get(key), second.get(key))
            node = self.node(
                key, 'nested', first.get(key), second.get(key), child
                )
            return node
        elif first.get(key) is None:
            node = self.node(key, 'added', None, second.get(key), None)
            return node
        elif second.get(key) is None:
            node = self.node(key, 'removed', first.get(key), None, None)
            return node
        elif self.check(first.get(key), second.get(key)):
            node = self.node(
                key, 'unchanged', first.get(key), second.get(key), None
                )
            return node
        elif not self.check(first.get(key), second.get(key)):
            node = self.node(
                key, 'changed', first.get(key), second.get(key), None
                )
            return node

    def parse(self, first=None, second=None):
        if first is None and second is None:
            first, second = self.data
        all_keys = {**first, **second}.keys()
        res = list(map(
                lambda k: self.switch(
                    k, first=first, second=second), all_keys))
        return res

    @staticmethod
    def check(first, second):
        if first == second:
            return True
        return False

    @staticmethod
    def node(key, type_, old, new, child):
        n = {
            '__key__': key,
            '__type__': type_,
            '__old__': old,
            '__new__': new,
            '__child__': child
        }
        return n

    @staticmethod
    def is_nested(first, second):
        if isinstance(first, dict) and isinstance(second, dict):
            return True
        return False
