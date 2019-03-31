class PrettyRender:
    def __init__(self, _ast):
        self._ast = _ast.parse()
        self.tab = '    '

    def render(self, _ast=None, count=0, template=''):
        def indents(count):
            return self.tab*count

        if _ast is None:
            _ast = self._ast
        if isinstance(_ast, list):
            for node in _ast:
                if node.get('__type__') == 'added':
                    res = '{}+ {}: {}\n'.format(
                        indents(count),
                        node.get('__key__'),
                        node.get('__new__'))
                    template += res
                elif node.get('__type__') == 'removed':
                    res = '\n{}- {}: {}\n'.format(
                        indents(count),
                        node.get('__key__'),
                        node.get('__old__'))
                    template += res
                elif node.get('__type__') == 'changed':
                    res = '\n{}+ {}: {}\n'.format(
                        indents(count),
                        node.get('__key__'),
                        node.get('__new__')
                        )
                    template += res
                    res = '\n{}- {}: {}\n'.format(
                        indents(count),
                        node.get('__key__'),
                        node.get('__old__')
                        )
                    template += res
                elif node.get('__type__') == 'nested':
                    if node.get('__child__') is not None:
                        res = '\n{}{}: {}\n'.format(
                            indents(count),
                            node.get('__key__'),
                            self.render(
                                _ast=node.get('__child__'),
                                count=(count+1)
                                )
                            )
                        template += res
                elif node.get('__type__') == 'unchanged':
                    res = '\n{}{}: {}\n'.format(
                        indents(count),
                        node.get('__key__'),
                        node.get('__old__'))
                    template += res
        return '{' + template + '{}'.format(indents(count)) + '}'
