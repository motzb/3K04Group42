import serial

running = True
while (running == True):
    #Open communication
    s = serial.Serial('COM3', baudrate = 115200, timeout = 10)
    print("Opening: " + s.name)

    #Define signals
    SYNC = 0x16

    FN = input("\n\n************************************\n\nEnter 's' to set parameters, 'r' to receive them from the board, or 'q' to quit the program\n")
    if (FN == "s"):
        FN_CODE = 0x55
    elif (FN == "r"):
        FN_CODE = 0x22
    else:
        running = False
        break

    RED_ENABLE = 1
    GREEN_ENABLE = 0xFF
    BLUE_ENABLE = 0xFF

    OFF_TIME = 2 #in seconds
    SWITCH_TIME = 500 #in milliseconds

    #Synch with board
    print("\n\n************************************\n\nSynching...")
    s.write(SYNC)
    s.write(FN_CODE)

    if (FN_CODE == 0x55):
        #Send parameters
        print("\nSending data...")
        s.write(RED_ENABLE)
        s.write(GREEN_ENABLE)
        s.write(BLUE_ENABLE)
        #OFF_TIME and SWITCH_TIME may require different send structure since they
        # are > 8 bits
        s.write(OFF_TIME) #4 uint bytes (single)
        s.write(SWITCH_TIME) #2 uint bytes (uint 16)
        
    else:
        print("\n\n************************************\n\nReceiving data...")
        #Receive parameters
        i = 0
        while (i <= 8):
            data_in[i] = s.read()
            #data_in[i] = data_in[i].decode() #(NOT SURE IF NECESSARY)
            i = i+1
        RED_ENABLE_in = data_in[0]
        print("\nRED_ENABLE = " + RED_ENABLE_in)
        GREEN_ENABLE_in = data_in[1]
        print("\nGREEN_ENABLE = " + RED_ENABLE_in)
        BLUE_ENABLE_in = data_in[2]
        print("\nBLUE_ENABLE = " + RED_ENABLE_in)
        OFF_TIME_in = data_in[3:6]
        print("\nOFF_TIME = " + RED_ENABLE_in)
        SWITCH_TIME_in = data_in[7:8]
        print("\nSWITCH_TIME = " + RED_ENABLE_in)
        
#Close communication
print("Closing: " + s.name)
s.close


