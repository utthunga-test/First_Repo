*** Settings ***
Library  modbus.py
Library  String
Library  Collections
*** Test Cases ***
Test case for connection
    ${connection}=    modbus.Connection
       log             ${connection}
    Should Be Equal     ${connection}   ${1}

#test cases for read only register with function code 4(input register)
# Test Cases for status

#     @{status}=        Create List    ${4660 }    ${22136}
#         Log List    ${status}
#     @{fun}=        modbus.func_04    ${30000}    ${2}
#         Log List    ${fun}
#     Lists Should Be Equal    ${fun}    ${status}



