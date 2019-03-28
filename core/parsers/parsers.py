import json
import hashlib


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
        self.result = {'change': {}, 'add': {}, 'remove': {}}

    def diff(self):
        first, second = self.data

        def check(first, second):
            first = hashlib.md5(str(first).encode('utf-8')).hexdigest()
            second = hashlib.md5(str(second).encode('utf-8')).hexdigest()
            if first == second:
                return False
            return True

        change = [k for k in first if k in second and check(first.get(k), second.get(k))]
        add = [k for k in second if k not in first]
        remove = [k for k in first if k not in second]
        if change:
            for k in change:
                self.result['change'].update({k:(first.get(k), second.get(k))})
        if add:
            for k in add:
                self.result['add'].update({k: second.get(k)})
        if remove:
            for k in remove:
                self.result['remove'].update({k: first.get(k)})
        return self.result
