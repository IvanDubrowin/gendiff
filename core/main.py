from .parsers import parsers
from .renders import json_render, plain_render, pretty_render
from .exceptions import FileFormatError


def main(first, second, format_=None):
    try:
        if first.endswith('json') and second.endswith('json'):
            loader = parsers.JsonLoader(first, second)
            diff = parsers.Differ(loader)
            return diff.diff_data()
    except AttributeError:
        raise FileFormatError
