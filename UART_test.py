import serial
import struct

#Open port
s = serial.Serial('COM3', baudrate = 115200, timeout = 10)
print("Opening: " + s.name)

#Initialize variables
reads = 0 #Used for tracking number of egram data reads
read_egram = 0 #Boolean for knowing when to take in egram data
atr_data = [] #Stores atrium egram data
vent_data = [] #Stores ventricle egram data
time = [] #Keepes track of time dimension for egram (using reads)

#---------------------------------------------------------------------------
#Sending parameters:
#---------------------------------------------------------------------------
#Set values (done within DCM by user)
SYNC = 22
pacingMode = 0 #uint8; 0-AOO,1-VOO,2-AAI,3-VVI,4-AAIR,5-VVIR
lowerRateLimit = 60 #uint8; ppm
pacingMode = 4 #uint8; 0-AOO,1-VOO,2-AAI,3-VVI,4-AAIR,5-VVIR
maxSensorRate = 120 #uint8; ppm
PaceAmp = 3.5 #single; V
PaceWidth = 0 #single; 0-30 ms
CMP_Amp = 2.5 #single; V
RefractoryPeriod = 250 #uint16; ms
activityThresh = 3 #uint8; V-Low,Low,Med-Low,Med,Med-High,High,V-High
reactionTime = 30 #uint8; s
responseFactor = 1 #uint8; 1-16
recoveryTime = 5 #uint8; 2-16 min
Save = 1 #uint8, denotes data should be saved in pacemaker

#To send connect flag ('connect' button clicked, but not save)
#board should update the user that the pacemaker and the DCM
#can communicate, but no update the internal parameters of the
#pacemaker
Save = 0 #set to 0 here so the internal paramters remain unchanged

#Pack data
SYNC = SYNC.to_bytes(1,'little')
pacingMode = pacingMode.to_bytes(1,'little')
lowerRateLimit = lowerRateLimit.to_bytes(1,'little')
maxSensorRate = maxSensorRate.to_bytes(1,'little')
PaceAmp = bytearray(struct.pack("<f",PaceAmp))
PaceWidth = bytearray(struct.pack("<f",PaceWidth))
CMP_Amp = bytearray(struct.pack("<f",CMP_Amp))
RefractoryPeriod = RefractoryPeriod.to_bytes(2,'little')
activityThresh = activityThresh.to_bytes(1,'little')
reactionTime = reactionTime.to_bytes(1,'little')
responseFactor = responseFactor.to_bytes(1,'little')
recoveryTime = recoveryTime.to_bytes(1,'little')
Save = Save.to_bytes(1,'little')

#Send data (but don't save on pacemaker)
print("\nSending connect packet")
s.write(SYNC)
s.write(pacingMode)
s.write(lowerRateLimit)
s.write(maxSensorRate)
s.write(PaceAmp)
s.write(PaceWidth)
s.write(CMP_Amp)
s.write(RefractoryPeriod)
s.write(activityThresh)
s.write(reactionTime)
s.write(responseFactor)
s.write(recoveryTime)
s.write(Save)

#Read connect back
connect_flag = s.read()
print("Connect flag received: ")
print("connect_flag", connect_flag)
if (connect_flag == 22):
    print("Connection successful :)")
else:
    print("Connection not successful :(")

#Send data (save on pacemaker)
Save = 1 #sent data pack will be saved on pacemaker
Save = Save.to_bytes(1,'little')

print("\nSending data to save in pacemaker")
#Send data
s.write(SYNC)
s.write(pacingMode)
s.write(lowerRateLimit)
s.write(maxSensorRate)
s.write(PaceAmp)
s.write(PaceWidth)
s.write(CMP_Amp)
s.write(RefractoryPeriod)
s.write(activityThresh)
s.write(reactionTime)
s.write(responseFactor)
s.write(recoveryTime)
s.write(Save)

#Check successful send
connect_flag = s.read(9)[0]
if (connect_flag == 22):
    print("Connection successful :)")
else:
    print("Connection not successful :(")
print("Save = ", Save)
    

#---------------------------------------------------------------------------
#Receiving egram data
#---------------------------------------------------------------------------
while (read_egram == 0):
    #Wait for read_egram == 33 to know that the pacemaker
    #will send egram data
    read_egram = s.read(9)[0]
while (read_egram == 33):
    #Receive and print bytes
    print("\nNow receiving egram data: ")
    data = s.read(9)
    print(data)
    
    #Packing data (note index at 0 since struct.unpack returns tuple)
    atr_data.append(struct.unpack("f",data[0:4])[0])
    vent_data.append(struct.unpack("f",data[4:8])[0])
    read_egram = data[9]

    time.append(float(reads))
    reads = reads + 1
    #For a test, we'll break this loop after 15 reads to check functin
    #in DCM, this could be done with some user input
    #(i.e. receive_egram == true)
    if (reads == 14):
        break

#Close communication
print("Closing: " + s.name)
s.close 

print("\nReceived data (now packed): ")
print("atr data:  ", atr_data)
print("vent data: ", vent_data)
print("time (ms): ", time)

    
