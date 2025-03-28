import argparse

from calli_cli.print import print_text
from calli_cli.render import render_text

def main():
    args = parse_args()
    # TODO get text from args
    text = "Hello"
    if args.render:
        render_text(text)
    else:
        print_text(text, args.port)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
            prog="calli", 
            description="Print stuff",
    )

    parser.add_argument("-r", "--render", action="store_true", help="render image rather than printing")
    parser.add_argument("-p", "--port", default="/dev/ttyACM0", help="Serial port, defaults to '/dev/ttyACM0'")
    #parser.add_argument('infile', type=argparse.FileType('r'), help="text file to print")
    return parser.parse_args()
