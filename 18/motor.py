import serial
ser = None
try:
    ser = serial.Serial('/dev/ttyUSB0')
except:
    try:
        ser = serial.Serial('/dev/ttyUSB1')
    except:
        try:
            ser = serial.Serial('/dev/ttyUSB2')
        except:
            ser = serial.Serial('/dev/ttyUSB3')


class Motor:
    id = -1
    dev = ser

    def __init__(self, n):
        id = n

    def run(self, n):
        self.dev.write(bytes(n, encoding='utf-8'))
