from HersheyFonts import HersheyFonts
from PIL import Image, ImageDraw


def render_text(text: str):
    # TODO figure out size
    width = 200
    height = 200
    img = Image.new("RGBA", (width, height), (255, 255, 255, 255))
    d = ImageDraw.Draw(img)

    thefont = HersheyFonts()
    thefont.load_default_font()
    thefont.normalize_rendering(50)

    # TODO do it one word at a time so we can do wrapping and stuff
    for (x1, y1), (x2, y2) in thefont.lines_for_text(text):
        d.line([(x1, height - y1), (x2, height - y2)], (0, 0, 0), width=1)

    img.show()
