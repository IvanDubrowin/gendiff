from .ast import AST
from .loaders import JsonLoader, YamlLoader
from .renders import json_render, plain_render, pretty_render
from .exceptions import FileFormatError


def main(first, second, format_=None):
    if first.endswith('json') and second.endswith('json'):
        loader = JsonLoader(first, second)
    elif first.endswith('yaml') and second.endswith('yaml'):
        loader = YamlLoader(first, second)
    else:
        raise FileFormatError
    diff = AST(loader)
    if format_ == 'plain':
        template = plain_render.PlainTextRender(diff)
    elif format_ == 'json':
        template = json_render.JsonRender(diff)
    else:
        template = pretty_render.PrettyRender(diff)
    return template.render()
