import serial
ser = serial.Serial('/dev/ttyUSB0',9600)
ser.write(bytes('M02550','UTF-8'))
