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
        return result
