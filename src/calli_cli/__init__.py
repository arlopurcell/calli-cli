import serial
import time

def find_calli_port() -> str:
    # TODO detect with serial.tools.list_ports and then filtering
    return "/dev/ttyACM0"

# Each shape fits in 20x20 square
shapes = {
    "square": [
        (2, 2),
        (18, 2),
        (18, 18),
        (2, 18),
        (2, 2),
    ],
    "triangle": [
        (2, 2),
        (10, 18),
        (18, 2),
        (2, 2),
    ],
    "hex": [
        (2, 10),
        (7, 18),
        (14, 18),
        (18, 10),
        (14, 2),
        (7, 2),
        (2, 10)
    ],
}

def main():
    port = find_calli_port()
    with serial.Serial(port) as ser:
        to_draw = ["square", "triangle", "hex", "triangle", "hex", "square"]
        base_x, base_y = (50, 50)
        for shape in to_draw:
            for x, y in shapes[shape]:
                command = f"G0 X{base_x + x} Y{base_y + y}\n" 
                print(command)
                ser.write(command.encode("utf-8"))
                # TODO wait for ACK
                time.sleep(1)
            base_x += 20


if __name__ == "__main__":
    main()

