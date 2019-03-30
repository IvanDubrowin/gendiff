from .ast import AST
from .loaders import JsonLoader
from .renders import json_render, plain_render, pretty_render


def main(first, second, format_=None):
    if first.endswith('json') and second.endswith('json'):
        loader = JsonLoader(first, second)
        diff = AST(loader)
        template = json_render.JsonRender(diff)
        return template.render()
