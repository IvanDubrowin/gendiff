class PlainTextRender:
    def __init__(self, _ast):
        self._ast = _ast.parse()
        self._template = []

    def render(self, _ast=None, path=''):
        result = ''
        if _ast is None:
            _ast = self._ast
        for node in _ast:
            if node.get('__type__') == 'nested':
                _loc_path = path + node.get('__key__') + '.'
                self.render(_ast=node.get('__child__'), path=_loc_path)
            else:
                self.get_template(node, path)
        for line in self._template:
            result += '{}\n'.format(line)
        return result

    def get_template(self, node, path):
        if node.get('__type__') == 'added':
            result = 'Property "{}{}" was added with value: "{}"'.format(
                path,
                node.get('__key__'),
                self.check_value(node.get('__new__'))
                )
            self._template.append(result)
        elif node.get('__type__') == 'removed':
            result = 'Property "{}{}" was removed'.format(
                path,
                node.get('__key__'))
            self._template.append(result)
        elif node.get('__type__') == 'changed':
            result = 'Property "{}{}" was updated. From "{}"​ to "{}"'.format(
                path,
                node.get('__key__'),
                node.get('__old__'),
                node.get('__new__')
            )
            self._template.append(result)

    @staticmethod
    def check_value(val):
        if isinstance(val, (list, set, tuple, dict)):
            return '[complex value]'
        return val
