from pymodbus.client.sync import ModbusSerialClient
from pymodbus.pdu import ModbusResponse, ExceptionResponse

client = ModbusSerialClient(

    method='rtu',

    port='COM7',

    baudrate=9600,

    timeout=0.05,

    parity='N',

    stopbits=1,

    bytesize=8

)

def connection():
    if not client.connect():
        return 0
    else:
        return 1
    
def func_04(adress, count):
    if client.connect():
        res = client.read_input_registers(address=30000,cout=2,unit=1)

        if not res.isError():

            print(res.registers)
        else:
            print(res)
        return ((res.resgisters))
    else:
        print('cannot connect to the Modbus Server/Slave')

