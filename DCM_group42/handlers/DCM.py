import serial
import struct

#Open port


#---------------------------------------------------------------------
#Test 1: Send in parameters and receive the, back
#---------------------------------------------------------------------

class Connection1:

    def __init__(self):
        #s = serial.Serial('COM3', baudrate = 115200, timeout = 10)
        #print("Opening: " + s.name)
        #Define data
        print("Initialzing connection object")
    def send_data(self, pm, lrl, rfctrp, athr, rt, rf, rcvt, msr, paceamp, pacewidth, rateAdapt, extr):
        s = serial.Serial('COM3', baudrate = 115200, timeout = 10)
        #Pack data
        self.SYNC = 22 #uint8
        #uint8; 0-Off, 1-AOO, 2-VOO, 3-AAI, 4-VVI, 5-AAIR, 6-VVIR
        if (pm == 'AOO'):
            self.pacingMode = 1
        elif (pm == 'VOO'):
            self.pacingMode = 2
        elif (pm == 'AAI'):
            self.pacingMode = 3
        elif (pm == 'VVI'):
            self.pacingMode = 4
        elif (pm == 'AOOR'):
            self.pacingMode = 5
        elif (pm == 'VOOR'):
            self.pacingMode = 6
        elif (pm == 'AAIR'):
            self.pacingMode = 7
        elif (pm == 'VVIR'):
            self.pacingMode = 8
        self.rateAdaptive = rateAdapt #uint8; 0-off, 1-on
        self.lowerRateLimit = lrl #uint8; ppm
        self.PaceAmp = paceamp #single; V
        self.PaceWidth = pacewidth #single; 0-30 ms
        self.CMP_Amp = 1.3 #single; V
        self.RefractoryPeriod = rfctrp #uint16; ms
        self.activityThresh = athr #uint8; V-Low,Low,Med-Low,Med,Med-High,High,V-High
        self.reactionTime = rt #uint8; s
        self.responseFactor = rf #uint8; 1-16
        self.recoveryTime = rcvt #uint8; 2-16 min
        self.maxSensorRate = msr #uint8; ppm
        self.extract = extr #0-don't send egram data, 1-send egram data
        
        print("\nSending data")
        #Pack data
        print("SYNC =", self.SYNC)
        SYNC = self.SYNC.to_bytes(1,'little')
        print("pacingMode =", self.pacingMode)
        pacingMode = self.pacingMode.to_bytes(1,'little')
        print("rateAdaptive=", self.rateAdaptive)
        rateAdaptive = self.rateAdaptive.to_bytes(1,'little')
        print("lowerRateLimit =", self.lowerRateLimit)
        lowerRateLimit = self.lowerRateLimit.to_bytes(1,'little')
        print("PaceAmp =", self.PaceAmp)
        PaceAmp = bytearray(struct.pack("<f",self.PaceAmp))
        print("PaceWidth =", self.PaceWidth)
        PaceWidth = bytearray(struct.pack("<f",self.PaceWidth))
        print("CMP_Amp =", self.CMP_Amp)
        CMP_Amp = bytearray(struct.pack("<f",self.CMP_Amp))
        print("RefractoryPeriod =", self.RefractoryPeriod)
        RefractoryPeriod = self.RefractoryPeriod.to_bytes(2,'little')
        print("activityThresh =", self.activityThresh)
        activityThresh = self.activityThresh.to_bytes(1,'little')
        print("reactionTime =", self.reactionTime)
        reactionTime = self.reactionTime.to_bytes(1,'little')
        print("responseFactor =", self.responseFactor)
        responseFactor = self.responseFactor.to_bytes(1,'little')
        print("recoveryTime =", self.recoveryTime)
        recoveryTime = self.recoveryTime.to_bytes(1,'little')
        print("maxSensorRate =", self.maxSensorRate)
        maxSensorRate = self.maxSensorRate.to_bytes(1,'little')
        print("extract =", self.extract)
        extract = self.extract.to_bytes(1,'little')
        
        #Send data
        s.write(SYNC)
        s.write(pacingMode)
        s.write(rateAdaptive)
        s.write(lowerRateLimit)
        s.write(PaceAmp)
        s.write(PaceWidth)
        s.write(CMP_Amp)
        s.write(RefractoryPeriod)
        s.write(activityThresh)
        s.write(reactionTime)
        s.write(responseFactor)
        s.write(recoveryTime)
        s.write(maxSensorRate)
        s.write(extract)
            # = 24 frames
        s.close()
    def receive_data(self):
        s = serial.Serial('COM3', baudrate = 115200, timeout = 10)
        reads = 0 #defines number of reads
        
        data_in = s.read(32)
        
        #Read egram
        atr_data_in = struct.unpack("f",data_in[0:4])[0]
        vent_data_in = struct.unpack("f",data_in[4:8])[0]
        read_egram = data_in[8]
        
        #Read echo
        pacingMode_back = data_in[9]
        rateAdaptive_back = data_in[10]
        lowerRateLimit_back = data_in[11]
        PaceAmp_back = struct.unpack("f", data_in[12:16])[0]
        PaceWidth_back = struct.unpack("f", data_in[16:20])[0]
        CMP_Amp_back = struct.unpack("f",data_in[20:24])[0]
        RefractoryPeriod_back = struct.unpack("H",data_in[24:26])[0]
        activityThresh_back = data_in[26]
        reactionTime_back = data_in[27]
        responseFactor_back = data_in[28]
        recoveryTime_back = data_in[29]
        maxSensorRate_back = data_in[30]
        extract_back = data_in[31]
        print("egram_data =", read_egram)
        
        #Printing to check correct data
        print("\nReceiving this back:")
        print("pacingMode =", pacingMode_back)
        print("rateAdaptive =", rateAdaptive_back)
        print("lowerRateLimit =", lowerRateLimit_back)
        print("PaceAmp =", PaceAmp_back)
        print("PaceWidth =", PaceWidth_back)
        print("CMP_Amp =", CMP_Amp_back)
        print("RefractoryPeriod =", RefractoryPeriod_back)
        print("activityThresh =", activityThresh_back)
        print("reactionTime =", reactionTime_back)
        print("responseFactor =", responseFactor_back)
        print("recoveryTime =", recoveryTime_back)
        print("maxSensorRate =", maxSensorRate_back)
        print("extract =", extract_back)
        
        return atr_data_in, vent_data_in, read_egram
        
        s.close()
        return to_return
    def close(self):
        #Close communication
        print("Closing: " + self.s.name)
        self.s.close 
