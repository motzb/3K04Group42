import serial
import struct

running = False
s = serial.Serial('COM3', baudrate = 115200, timeout = 10)
print("Opening: " + s.name)

#Define variables:
SYNC = 22
FN = input("Would you like to send ('s') or receive ('r') parameters? ")
if FN == 's':
    FN_CODE = 55
else:
    FN_CODE = 22
RED_ENABLE = 1
GREEN_ENABLE = 1
BLUE_ENABLE = 1
OFF_TIME = 1.3 #in seconds
SWITCH_TIME = 500 #in milliseconds

#Convert integer to bytes:
SYNC = SYNC.to_bytes(1,'little')
FN_CODE = FN_CODE.to_bytes(1,'little')
RED_ENABLE = RED_ENABLE.to_bytes(1,'little')
GREEN_ENABLE = GREEN_ENABLE.to_bytes(1,'little')
BLUE_ENABLE = BLUE_ENABLE.to_bytes(1,'little')
#Convert type single (float) to bytes in big endian format
#see https://docs.python.org/3/library/struct.html for more details
#and more data types.
OFF_TIME = bytearray(struct.pack("<f", OFF_TIME))
SWITCH_TIME = SWITCH_TIME.to_bytes(2,'little')

#Send parameters
if (FN == 's'):
    print("\nNow sending data")
    print("Sending " + str(SYNC))
    s.write(SYNC)
    print("Sending " + str(FN_CODE))
    s.write(FN_CODE)
    print("Sending " + str(RED_ENABLE))
    s.write(RED_ENABLE)
    print("Sending " + str(GREEN_ENABLE))
    s.write(GREEN_ENABLE)
    print("Sending " + str(BLUE_ENABLE))
    s.write(BLUE_ENABLE)
    print("Sending " + str([ "0x%02x" % b for b in OFF_TIME ]))
    s.write(OFF_TIME)
    print("Sending " + str(SWITCH_TIME))
    s.write(SWITCH_TIME)
else:
    #Sending 11 frames (to trigger UART send)
    s.write(SYNC)
    s.write(FN_CODE)
    s.write(RED_ENABLE)
    s.write(GREEN_ENABLE)
    s.write(BLUE_ENABLE)
    s.write(OFF_TIME)
    s.write(SWITCH_TIME)

    data_in = []
    #Reading values returned
    print("\nReading...")
    for i in range(9):
        data_in.append(s.read())

    print("RED_ENABLE =", data_in[0])
    print("GREEN_ENABLE =", data_in[1])
    print("BLUE_ENABLE =", data_in[2])
    print("OFF_TIME =", data_in[3:7])
    print("SWITCH_TIME =", data_in[7:9])

#Close communication
print("Closing: " + s.name)
s.close


