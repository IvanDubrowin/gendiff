import argparse
from core import __version__
from core.main import main


parser = argparse.ArgumentParser(
    usage='gendiff [options] <firstConfig> <secondConfig>',
    description='Compares two configuration files and shows a difference.'
    )
parser.add_argument(
    '-v', '--version',
    action='version',
    version='%(prog)s'+f' {__version__}'
    )
parser.add_argument(
    '-f', '--format',
    help='Output format',
    nargs=1,
    metavar=('[type]')
    )
parser.add_argument('firstConfig')
parser.add_argument('secondConfig')
args = parser.parse_args()

if __name__ == '__main__':
    namespace = vars(args)
    if namespace.get('firstConfig') is not None:
        main(first=namespace.get('firstConfig'),
             second=namespace.get('secondConfig'),
             format_=namespace.get('format'))
