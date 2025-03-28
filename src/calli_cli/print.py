from HersheyFonts import HersheyFonts
import serial


def print_text(text: str, font: HersheyFonts, port: str):
    base_x, base_y = (50, -70)

    last_point = (0, 0)
    with serial.Serial(port) as ser:
        for (x1, y1), (x2, y2) in font.lines_for_text(text):
            p1 = (x1 + base_x, -y1 + base_y)
            p2 = (x2 + base_x, -y2 + base_y)

            if p1 != last_point:
                pen_up(ser)
                move(p1, ser)
                pen_down(ser)

            move(p2, ser)
            last_point = p2

        # Return to starting point
        pen_up(ser)
        move((219, 0), ser)
        pen_down(ser)


def move(point: tuple[int, int], ser: serial.Serial):
    (x, y) = point
    send_cmd(f"G0 X{x} Y{y}", ser)


def pen_up(ser: serial.Serial):
    send_cmd("G0 Z10", ser)


def pen_down(ser: serial.Serial):
    send_cmd("G0 Z0", ser)


def send_cmd(cmd: str, ser: serial.Serial):
    print(cmd)
    ser.write((cmd + "\n").encode("utf-8"))
    resp = ser.readline().decode("utf-8")
    if resp.strip() != "OK":
        raise Exception(resp)
