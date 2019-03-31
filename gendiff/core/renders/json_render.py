import json
from collections import OrderedDict
from .pretty_render import PrettyRender

class JsonRender():
    def __init__(self, _ast):
        self._ast = _ast.parse()
        self._template = OrderedDict()

    def parse(self, _ast=None):
        if _ast is None:
            _ast = self._ast
        if isinstance(_ast, list):
            for node in _ast:
                if node.get('__type__') == 'added':
                    res = {'+ ' + node.get('__key__'): node.get('__new__')}
                    self._template.update(res)
                elif node.get('__type__') == 'removed':
                    res = {'- ' + node.get('__key__'): node.get('__old__')}
                    self._template.update(res)
                elif node.get('__type__') == 'changed':
                    res = {'+ ' + node.get('__key__'): node.get('__new__')}
                    self._template.update(res)
                    res = {'- ' + node.get('__key__'): node.get('__old__')}
                    self._template.update(res)
                elif node.get('__type__') == 'nested':
                    if node.get('__child__') is not None:
                        res = {node.get('__key__'):
                            self.parse(_ast=node.get('__child__'))}
                        self._template.update(res)
                elif node.get('__type__') == 'unchanged':
                    res = {node.get('__key__'): node.get('__old__')}
                    self._template.update(res)

    def render(self):
        self.parse()
        return json.dumps(dict(self._template), indent=4)
