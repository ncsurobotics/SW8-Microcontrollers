import serial
ser = serial.Serial('/dev/ttyACM0')
print(ser.name)
print(ser.readline())
#WaitFor7E
ser.write('X')
print(ser.readline())
#WaitForFF
ser.write('A')
print(ser.readline())
#Read
ser.write('C')
print(ser.readline())
#Address
ser.write('T')
print(ser.readline())
#read depthVal
print(ser.readline())
#WaitFor7E
