from HersheyFonts import HersheyFonts
import serial

#def print_symbols(symbols: list[Symbol], port: str):
#    with serial.Serial(port) as ser:
#        to_draw = ["square", "triangle", "hex"]
#        base_x, base_y = (100, -140)
#        for symbol in symbols:
#            send_cmd(f"G0 Z5", ser)
#
#            for (x, y) in symbol.points:
#                send_cmd(f"G0 X{base_x + x} Y{base_y + y}", ser)
#                send_cmd(f"G0 Z0", ser)
#            send_cmd(f"G0 Z5", ser)
#            base_x += symbol.width
#        send_cmd(f"G0 X0 Y0", ser)
#        send_cmd(f"G0 Z0", ser)

def print_text(text: str, port: str):
    base_x, base_y = (50, 140)
    
    thefont = HersheyFonts()
    thefont.load_default_font()
    thefont.normalize_rendering(30)
    
    last_point = (0, 0)
    with serial.Serial(port) as ser:
        for (x1, y1), (x2, y2) in thefont.lines_for_text(text):
            p1 = (x1 + base_x, y1 + base_y)
            p2 = (x2 + base_x, y2 + base_y)

            if p1 != last_point:
                send_cmd("G0 Z5", ser)
                send_cmd(f"G0 X{p1[0]} Y{p1[1]}", ser)
                send_cmd("G0 Z0", ser)
                
            send_cmd(f"G0 X{p2[0]} Y{p2[1]}", ser)
            last_point = p2
        
def send_cmd(cmd: str, ser: serial.Serial):
    print(cmd)
    ser.write((cmd + "\n").encode("utf-8"))
    resp = ser.readline().decode("utf-8")
    if resp.strip() != "OK":
        print(resp)

