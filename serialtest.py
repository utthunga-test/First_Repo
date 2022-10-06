import serial
import time

class serialtest(object):
    def test(self,a):
        ser = serial.Serial ('COM4')    #Open named port
        ser.baudrate = 9600           #Set baud rate to 9600
        #Read ten characters from serial port to data
<<<<<<< HEAD
        ser.write(b'welcome to star123')
=======
        ser.write(b'welcome to star12')
>>>>>>> 4c03e2e818e57ccb736f0dd53d1b3a54a68e413f
        time.sleep(1)
        data1 = ser.read(16)
        return data1
        #Send back the received data
        ser.close()

   

# a=serialtest()

# print(a.test(a))
