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
