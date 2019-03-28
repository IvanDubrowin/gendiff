from .parsers import parsers
from .renders import json_render, plain_render, pretty_render


def main(first, second, format_=None):
    if first.endswith('json') and second.endswith('json'):
        loader = parsers.JsonLoader(first, second)
        diff = parsers.Differ(loader)
        template = json_render.JsonRender(diff)
        return template.render()
