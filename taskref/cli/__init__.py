from argparse import ArgumentParser

from taskref import __version__


def build_parser():
    parser = ArgumentParser(prog='taskref')
    parser.add_argument('--version', action='version', version=f'taskref {__version__}')
    return parser


def main():
    args = build_parser().parse_args()
