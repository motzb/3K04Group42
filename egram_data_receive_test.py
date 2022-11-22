import serial
import struct

#Open port
s = serial.Serial('COM3', baudrate = 115200, timeout = 10)
print("Opening: " + s.name)
reads = 0
atr_data = []
vent_data = []
time = []
while reads < 10:
    #Receive and print bytes
    print("\nNow receiving data: ")
    data = s.read(8)
    print(data)

    #Packing data (note index at 0 since struct.unpack returns tuple)
    atr_data.append(struct.unpack("f",data[0:4])[0])
    vent_data.append(struct.unpack("f",data[4:8])[0])

    time.append(float(reads))
    reads = reads + 1

#Close communication
print("Closing: " + s.name)
s.close 

print("\nReceived data (now packed): ")
print("atr data:  ", atr_data)
print("vent data: ", vent_data)
print("time (ms): ", time)

    
