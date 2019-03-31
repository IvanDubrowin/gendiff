import json
from .pretty_render import PrettyRender

class JsonRender():
    def __init__(self, _ast):
        self.template = PrettyRender(_ast)

    def render(self):
        template = self.template.render().strip('""')
        template = template.splitlines()
        return json.dumps(template, indent=4)
