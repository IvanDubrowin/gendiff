class PrettyRender:
    def __init__(self, _ast):
        self._ast = _ast.parse()

    def render(self, _ast=None, template=''):
        if _ast is None:
            _ast = self._ast
        if isinstance(_ast, list):
            for node in _ast:
                if node.get('__type__') == 'added':
                    res = '\n\t\t+ {}: {}'.format(
                        node.get('__key__'), node.get('__new__'))
                    template += res
                elif node.get('__type__') == 'removed':
                    res = '\n\t\t- {}: {}'.format(
                        node.get('__key__'), node.get('__old__'))
                    template += res
                elif node.get('__type__') == 'changed':
                    res = '\n\t\t+ {}: {}\n\t- {}: {}'.format(
                        node.get('__key__'), node.get('__new__'),
                        node.get('__key__'), node.get('__old__')
                        )
                    template += res
                elif node.get('__type__') == 'nested':
                    if node.get('__child__') is not None:
                        res = '\n\t{}: {}'.format(
                            node.get('__key__'),
                            self.render(_ast=node.get('__child__'))
                            )
                        template += res
                elif node.get('__type__') == 'unchanged':
                    res = '\n\t\t{}: {}'.format(
                        node.get('__key__'), node.get('__old__'))
                    template += res
        return '{' + template + '\n}'
