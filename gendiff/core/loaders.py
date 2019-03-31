import json
import yaml
from abc import ABC, abstractmethod


class AbstractLoader(ABC):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    @abstractmethod
    def load(self):
        raise NotImplementedError


class JsonLoader(AbstractLoader):
    def load(self):
        with open(self.first, 'r') as f:
            first = json.load(f)

        with open(self.second, 'r') as f:
            second = json.load(f)
        return first, second


class YamlLoader(AbstractLoader):
    def load(self):
        with open(self.first) as f:
            first = yaml.load(f)

        with open(self.second) as f:
            second = yaml.load(f)

        return first, second
