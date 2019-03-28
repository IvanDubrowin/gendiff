import json
from collections import OrderedDict, ChainMap


class JsonRender:
    def __init__(self, differ):
        self.data = differ.data
        self.diff_data = differ.diff_data()
        self._template = OrderedDict()

    def render(self):
        if self.diff_data.get('change') is not None:
            change_dict = self.diff_data.get('change')
        else:
            change_dict = {}

        if self.diff_data.get('add') is not None:
            add_dict = self.diff_data.get('add')
        else:
            add_dict = {}

        if self.diff_data.get('remove') is not None:
            remove_dict = self.diff_data.get('remove')
        else:
            remove_dict = {}

        chain = ChainMap(change_dict, add_dict, remove_dict)
        for key in self.data[0]:
            if key not in chain:
                self._template.update({key: self.data[0][key]})

        if change_dict:
            for item in change_dict.items():
                self._template.update({'+ '+ item[0]: item[1][1]})
                self._template.update({'- '+ item[0]: item[1][0]})

        if add_dict:
            for item in add_dict.items():
                self._template.update({'+ '+ item[0]: item[1]})

        if remove_dict:
            for item in remove_dict.items():
                self._template.update({'- '+ item[0]: item[1]})

        return json.dumps(dict(self._template), indent=2)
