import json
from dictdiffer import diff


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
        self.diff = {}

    def diff_data(self):
        result = diff(self.data[0], self.data[1])

        if result:
            for i in result:
                if i[0] == 'change':
                    if self.diff.get(i[0]) is not None:
                        self.diff[i[0]].update({i[1]: i[2]})
                    else:
                        self.diff[i[0]] = {i[1]: i[2]}
                else:
                    if isinstance(i[2], list):
                        self.diff[i[0]] = dict(i[2])
        return self.diff
