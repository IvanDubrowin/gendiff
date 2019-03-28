import json


class JsonLoader:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def load(self):
        with open(self.first, 'r') as f:
            first = json.load(f)

        with open(self.second, 'r') as f:
            second = json.load(f)
        return first, second


class YamlLoader:
    pass


class Differ:
    def __init__(self, loader):
        self.data = loader.load()
        self.result = {
            'change': {},
            'add': {},
            'remove': {},
            'unchange': {}
            }

    def unchanged(self, first, second):
        for k in first:
            if k in second and self.check(first.get(k), second.get(k)):
                self.result['unchange'].update({k: first.get(k)})

    def changed(self, first, second):
        for k in first:
            if k in second and not self.check(first.get(k), second.get(k)):
                if not isinstance(first.get(k), dict) and \
                        not isinstance(second.get(k), dict):
                    self.result['change'].update({k: first.get(k)})

    def added(self, first, second):
        for k in second:
            if k not in first:
                self.result['add'].update({k: second.get(k)})

    def removed(self, first, second):
        for k in first:
            if k not in second:
                self.result['remove'].update({k: first.get(k)})

    def nested(self, first, second):
        for k in second:
            if not self.check(first.get(k), second.get(k)):
                if isinstance(first.get(k), dict) and \
                        isinstance(second.get(k), dict):
                    self.diff(first=first.get(k), second=second.get(k))

    def diff(self, first=None, second=None):
        if first is None and second is None:
            first, second = self.data
        tokens = [
            self.unchanged,
            self.changed,
            self.added,
            self.removed,
            self.nested
            ]
        for token in tokens:
            token(first, second)
        return self.result

    @staticmethod
    def check(first, second):
        if first == second:
            return True
        return False
