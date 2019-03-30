import re
import json
from .pretty_render import PrettyRender

class JsonRender():
    def __init__(self, _ast):
        self.template = PrettyRender(_ast)

    def render(self):
        template = self.template.render()
        return json.dumps(template, indent=4)
