import json
from collections import OrderedDict, ChainMap

KEYS = [
    'unchange',
    'change',
    'add',
    'remove'
]

class JsonRender:
    def __init__(self, differ):
        self.diff = differ.diff()

    def render(self, diff=None):
        if diff is None:
            diff = self.diff
        _template = {}

        for k in diff:
            if k == 'unchange' and not isinstance(diff.get(k), dict):
                _template.update({k: diff.get(k)})
            elif k == 'unchange' and isinstance(diff.get(k), dict)\
                and diff.get(k) is not None:
                print(diff.get(k))
                _template.update({self.render(diff=diff.get(k))})
            elif k == 'change':
                if diff.get('change'):
                    change_dict = self.get('change')
                    for item in change_dict.items():
                        _template.update({'+ '+ item[0]: item[1]})
                        _template.update({'- '+ item[0]: item[1]})
            elif k == 'add':
                if diff.get('add'):
                    add_dict = diff.get('add')
                    for item in add_dict.items():
                        _template.update({'+ '+ item[0]: item[1]})
            elif k == 'remove':
                if diff.get('remove'):
                    remove_dict = diff.get('remove')
                    for item in remove_dict.items():
                        _template.update({'- '+ item[0]: item[1]})
        return json.dumps(_template, indent=2)
