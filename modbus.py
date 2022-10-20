<<<<<<< HEAD
from pymodbus.client.sync import ModbusSerialClient

client = ModbusSerialClient(

    method='rtu',

    port='COM2',

    baudrate=9600,

    timeout=0.05,

    parity='N',

    stopbits=1,

    bytesize=8

)



if client.connect():

    res = client.read_input_registers(address=30000,cout=2,unit=1)

    if not res.isError():

        print(res.registers)

    else:

        print(res)

else:

    print('cannot connect to the Modbus Server/Slave')
=======
from pymodbus.client.sync import ModbusSerialClient

client = ModbusSerialClient(

    method='rtu',

    port='COM2',

    baudrate=9600,

    timeout=0.05,

    parity='N',

    stopbits=1,

    bytesize=8

)



if client.connect():

    res = client.read_input_registers(address=30000,cout=2,unit=1)

    if not res.isError():

        print(res.registers)

    else:

        print(res)

else:

    print('cannot connect to the Modbus Server/Slave')
>>>>>>> 42003cd2bc27782be5c0043c135cc92797d99a68
