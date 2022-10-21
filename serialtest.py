import serial
import time

class serialtest(object):
    def test(self):
        ser = serial.Serial ("COM3")    #Open named port
        ser.baudrate = 9600           #Set baud rate to 9600
        #Read ten characters from serial port to data
        ser.write(b'hello world')
        time.sleep(1)
        data1 = ser.read(11)
        print(data1)
        #Send back the received data
        ser.close()

a=serialtest()

a.test()