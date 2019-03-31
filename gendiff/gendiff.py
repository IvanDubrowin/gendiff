'''Usage:
    gendiff.py [options] <firstConfig> <secondConfig>

   Compares two configuration files and shows a difference.

   Options:
    -h --​help  output usage information
    -v --version  output the version number
    -f --format [​type​]  Output format
'''
import sys
from docopt import docopt
from core import __version__
from core.main import main


if __name__ == '__main__':
    namespace = docopt(__doc__, version=__version__)
    if namespace.get('<firstConfig>') is not None:
        res = main(first=namespace.get('<firstConfig>'),
                   second=namespace.get('<secondConfig>'),
                   format_=namespace.get('--format'))
        sys.stdout.write(res)
