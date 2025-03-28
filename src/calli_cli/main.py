import argparse

from HersheyFonts import HersheyFonts

from calli_cli.print import print_text
from calli_cli.render import render_text


def main():

    args = parse_args()

    # TODO get text from args
    text = "Hello"

    font = HersheyFonts()
    font.load_default_font(args.font_style + args.font_type)
    font.normalize_rendering(args.size)

    if args.render:
        render_text(text, font)
    else:
        print_text(text, font, args.port)


def parse_args() -> argparse.Namespace:
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
        "--font-style",
        default="rowman",
        choices=[
            "rowman",
            "greek",
            "italic",
            "script",
            "cyril",
        ],
        help="font style",
    )
    parser.add_argument(
        "--font-type",
        default="s",
        choices=["p", "s", "d", "c", "t", "cs"],
        help="font type",
    )
    parser.add_argument(
        "-s",
        "--size",
        type=int,
        default=50,
        help="Size of font in unknown units, defaults to 50",
    )
    # parser.add_argument(
    #     'infile',
    #     type=argparse.FileType('r'),
    #     help="text file to print",
    # )
    return parser.parse_args()
