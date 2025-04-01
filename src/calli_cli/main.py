import argparse
import sys

from HersheyFonts import HersheyFonts

from calli_cli.print import print_text
from calli_cli.render import render_text


def main():
    font = HersheyFonts()

    args = parse_args(font)

    text = args.infile.read()

    font.load_default_font(args.font)
    font.normalize_rendering(args.size)

    if args.render:
        render_text(text, font)
    else:
        print_text(text, font, args.port)


def parse_args(font: HersheyFonts) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
            prog="calli",
            description="Print stuff",
    )

    parser.add_argument(
        "-r",
        "--render",
        action="store_true",
        help="render image rather than printing",
    )
    parser.add_argument(
        "-p",
        "--port",
        default="/dev/ttyACM0",
        help="Serial port, defaults to '/dev/ttyACM0'",
    )
    parser.add_argument(
        "-f",
        "--font",
        default="rowmans",
        choices=font.default_font_names,
        help="font name",
    )
    parser.add_argument(
        "-s",
        "--size",
        type=int,
        default=50,
        help="Size of font in unknown units, defaults to 50",
    )
    parser.add_argument(
        'infile',
        type=argparse.FileType('r'),
        default=sys.stdin,
        help="text file to print, defaults to stdin",
    )
    return parser.parse_args()
