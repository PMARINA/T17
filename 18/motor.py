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
        self.id = n

    def run(self, n):
        print('M'.strip() + str(self.id).strip() +
              str(n).strip())
        self.dev.write(bytes('M'.strip() + str(self.id).strip() +
                             str(n.zfill(4)).strip(), encoding='utf-8'))
