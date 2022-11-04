import serial
import time
class serialtest(object):
    def test(self):
        ser = serial.Serial ('/dev/ttyUSB0')                                      
        ser.baudrate = 9600           
        #Read ten characters from serial port to data
        ser.write(b'hi')
        time.sleep(1)
        data1 = ser.read(11)
        print(data1)
        #Send back the received data
        ser.close()

a=serialtest()
a.test()