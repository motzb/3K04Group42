from functools import partial

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QSpinBox, QDoubleSpinBox, QComboBox, QRadioButton
import numpy as np 
import matplotlib.pyplot as plt 
import time
import json

from views.dashboard import Ui_Dashboard
from handlers.DCM import Connection1


class Graph:
    def graphdata(self, time, signalatr, signalvent):
        #plots and shows the graph
        fig, axs = plt.subplots(2) 
        axs[0].plot(time,signalatr)
        axs[0].set_title("Atrial Signal")
        axs[0].set(xlabel="time")
        axs[0].set(ylabel="heart signal")
        axs[1].plot(time,signalvent)
        axs[1].set_title("Ventricle Signal")
        axs[1].set(xlabel="time")
        axs[1].set(ylabel="heart signal")
        plt.tight_layout()
        plt.show()
"""
#test case
x=[1,2,3,4,5,6]
y=[0,62,57,88,69,90]
y2=[60,62,57,88,69,90]
graphdata(x,y,y2)
"""

# Dashboard controller class that will handle all the events of the widgets in the dashboard view
class Dashboard(QMainWindow, Ui_Dashboard):
    def __init__(self, parent):
        super(Dashboard, self).__init__()
        self.setupUi(self)
        self.username = None
        self.parent = parent
        self.unique = {}
        self.storage = {}
        self.egrams = {}
        self.a_mode = None
        self.transmitting = False
        self.pacemaker_data = None
        self._conn = None
        self._pacing_modes = {
            "AOO":1,
            "VOO":2,
            "AAI":3,
            "VVI":4,
            "AOOR":5,
            "VOOR":6,
            "AAIR":7,
            "VVIR":8
        }
        self.atr_data = []
        self.vent_data = []
        self.time_data = []
        self.ups = [
            "Lower Rate Limit"
            "Upper Rate Limit",
            "Maximum Sensor Rate",
            "Fixed AV Delay",
            "Atrial Amplitude"
            "Atrial Pulse Width"
            "Atrial Sensitivity"
            "Ventricular Amplitude"
            "Ventricular Pulse Width"
            "Ventricular Sensitivity",
            "ARP",
            "VRP",
            "PVARP",
            "Activity Threshold",
            "Reaction Time",
            "Response Factor",
            "Recovery Time"]
        self.ds = {}

    # to initialize the dashboard view after login for a particular user
    def init(self, username):
        self.username = username
        self.label_welcome.setText("Hi, {}".format(self.username))
        try:
            with open("data.json", "r") as f:
                self.storage = json.loads(f.read())
                self.unique = self.storage[self.username]
                print(self.unique)
        except:
            pass
        #self.unique = self.storage[self.username]

    # function overriding, setupUi function setup call for widgets
    def setupUi(self, Dashboard):
        Ui_Dashboard.setupUi(self, Dashboard)

        # click handlers of the buttons in the ui
        self.spinBox_lrl.valueChanged.connect(self.on_lrl_changed)
        #self.lineEdit_va.valueChanged.connect(self.on_av_changed)
        #self.lineEdit_av.valueChanged.connect(self.on_va_changed)
        self.spinBox_vpw.valueChanged.connect(self.on_vpw_changed)
        self.spinBox_apw.valueChanged.connect(self.on_vpw_changed)
        self.lineEdit_vrp_3.valueChanged.connect(self.on_a_sens_changed)
        self.lineEdit_vrp_4.valueChanged.connect(self.on_a_thr_changed)
        self.lineEdit_vrp_5.valueChanged.connect(self.on_v_sens_changed)
        self.btn_transmit_data.clicked.connect(self.transmit_data)
        self.export_ve.clicked.connect(self.export_venticular_egram)
        self.export_ae.clicked.connect(self.export_atrial_egram)
        self.export_ave.clicked.connect(self.export_both_egrams)
        #self.pushButton_save.clicked.connect(self.on_save_clicked)
        self.btn_logout.clicked.connect(self.onclick_btn_logout)
        for i, pacing_mode in enumerate(filter(lambda x: isinstance(x, QRadioButton),
                                               self.frame_pacing_modes.children())):
            pacing_mode.toggled.connect(self.pacing_mode_changed)
        self.frame_12.setVisible(False)
        self.frame_13.setVisible(False)
        self.frame_18.setVisible(False)
        self.frame_19.setVisible(False)
        self.frame_11.setVisible(False)
        self.frame_10.setVisible(False)
        self.frame_17.setVisible(False)
        self.frame_16.setVisible(False)
        self.frame_21.setVisible(False) # Maximum Sensor Rate
        self.frame_20.setVisible(False) # Atrial sens
        self.frame_23.setVisible(False) # Venticular sens
        self.frame_22.setVisible(False) # Activity Thr
        self.frame_25.setVisible(False) # Reaction time
        self.frame_26.setVisible(False) # Response factor
        self.frame_24.setVisible(False) # Recovery Time
        self.export_ae.setVisible(False)
        self.export_ve.setVisible(False)
        self.export_ave.setVisible(False)

    def export_atrial_egram(self):
        self.egrams["Atrial"] = None

    def export_venticular_egram(self):
        self.egrams["Venticular"] = None

    def export_both_egrams(self):
        self.egrams["Atrial"] = None
        self.egrams["Venticular"] = None
        #Send data
        if "V" in self.a_mode:
            if "R" in self.a_mode:
                self._conn.send_data(self.a_mode, self.spinBox_lrl.value(), self.lineEdit_vrp.value(), self.lineEdit_vrp_4.value(), self.lineEdit_vrp_7.value(), self.lineEdit_vrp_8.value(), self.lineEdit_vrp_6.value(), self.lineEdit_vrp_2.value(), self.lineEdit_va.value(), self.spinBox_vpw.value(), 1, 1)
            else:
                self._conn.send_data(self.a_mode, self.spinBox_lrl.value(), self.lineEdit_vrp.value(), self.lineEdit_vrp_4.value(), self.lineEdit_vrp_7.value(), self.lineEdit_vrp_8.value(), self.lineEdit_vrp_6.value(), self.lineEdit_vrp_2.value(), self.lineEdit_va.value(), self.spinBox_vpw.value(), 0, 1)
        else:
            if "R" in self.a_mode:
                self._conn.send_data(self.a_mode, self.spinBox_lrl.value(), self.lineEdit_arp.value(), self.lineEdit_vrp_4.value(), self.lineEdit_vrp_7.value(), self.lineEdit_vrp_8.value(), self.lineEdit_vrp_6.value(), self.lineEdit_vrp_2.value(), self.lineEdit_av.value(), self.spinBox_apw.value(), 1, 1)
            else:
                self._conn.send_data(self.a_mode, self.spinBox_lrl.value(), self.lineEdit_arp.value(), self.lineEdit_vrp_4.value(), self.lineEdit_vrp_7.value(), self.lineEdit_vrp_8.value(), self.lineEdit_vrp_6.value(), self.lineEdit_vrp_2.value(), self.lineEdit_av.value(), self.spinBox_apw.value(), 0, 1)
        
        read_egram = 1
        reads = 0
        while (read_egram == 1):
            self.time_data.append(reads)
            egram_data = self._conn.receive_data()
            self.atr_data.append(egram_data[0])
            self.vent_data.append(egram_data[1])
            read_egram = egram_data[2]
            reads = reads + 1
            print(reads)
            
            if (reads == 100):
                #Send data to stop transmission
                if "V" in self.a_mode:
                    if "R" in self.a_mode:
                        self._conn.send_data(self.a_mode, self.spinBox_lrl.value(), self.lineEdit_vrp.value(), self.lineEdit_vrp_4.value(), self.lineEdit_vrp_7.value(), self.lineEdit_vrp_8.value(), self.lineEdit_vrp_6.value(), self.lineEdit_vrp_2.value(), self.lineEdit_va.value(), self.spinBox_vpw.value(), 1, 0)
                    else:
                        self._conn.send_data(self.a_mode, self.spinBox_lrl.value(), self.lineEdit_vrp.value(), self.lineEdit_vrp_4.value(), self.lineEdit_vrp_7.value(), self.lineEdit_vrp_8.value(), self.lineEdit_vrp_6.value(), self.lineEdit_vrp_2.value(), self.lineEdit_va.value(), self.spinBox_vpw.value(), 0, 0)
                else:
                    if "R" in self.a_mode:
                        self._conn.send_data(self.a_mode, self.spinBox_lrl.value(), self.lineEdit_arp.value(), self.lineEdit_vrp_4.value(), self.lineEdit_vrp_7.value(), self.lineEdit_vrp_8.value(), self.lineEdit_vrp_6.value(), self.lineEdit_vrp_2.value(), self.lineEdit_av.value(), self.spinBox_apw.value(), 1, 0)
                    else:
                        self._conn.send_data(self.a_mode, self.spinBox_lrl.value(), self.lineEdit_arp.value(), self.lineEdit_vrp_4.value(), self.lineEdit_vrp_7.value(), self.lineEdit_vrp_8.value(), self.lineEdit_vrp_6.value(), self.lineEdit_vrp_2.value(), self.lineEdit_av.value(), self.spinBox_apw.value(), 0, 0)
        
        print("\nReceived egram data: ")
        print("atr data:  ", self.atr_data)
        print("vent data: ", self.vent_data)
        print("time (ms): ", self.time_data)
        g = Graph()
        g.graphdata(self.time_data, self.atr_data, self.vent_data)
        

    def transmit_data(self):
        self.transmitting = not self.transmitting
        if not self.a_mode:
            qm = QMessageBox()
            QMessageBox.information(qm, "Connection", "Select mode first!", QMessageBox.Ok, QMessageBox.Ok)
        if self.transmitting:
            print(self.transmitting)
            if not self._conn:
                self._conn = Connection1()
            #Send data
            if "V" in self.a_mode:
                if "R" in self.a_mode:
                    self._conn.send_data(self.a_mode, self.spinBox_lrl.value(), self.lineEdit_vrp.value(), self.lineEdit_vrp_4.value(), self.lineEdit_vrp_7.value(), self.lineEdit_vrp_8.value(), self.lineEdit_vrp_6.value(), self.lineEdit_vrp_2.value(), self.lineEdit_va.value(), self.spinBox_vpw.value(), 1, 1)
                else:
                    self._conn.send_data(self.a_mode, self.spinBox_lrl.value(), self.lineEdit_vrp.value(), self.lineEdit_vrp_4.value(), self.lineEdit_vrp_7.value(), self.lineEdit_vrp_8.value(), self.lineEdit_vrp_6.value(), self.lineEdit_vrp_2.value(), self.lineEdit_va.value(), self.spinBox_vpw.value(), 0, 1)
            else:
                if "R" in self.a_mode:
                    self._conn.send_data(self.a_mode, self.spinBox_lrl.value(), self.lineEdit_arp.value(), self.lineEdit_vrp_4.value(), self.lineEdit_vrp_7.value(), self.lineEdit_vrp_8.value(), self.lineEdit_vrp_6.value(), self.lineEdit_vrp_2.value(), self.lineEdit_av.value(), self.spinBox_apw.value(), 1, 1)
                else:
                    self._conn.send_data(self.a_mode, self.spinBox_lrl.value(), self.lineEdit_arp.value(), self.lineEdit_vrp_4.value(), self.lineEdit_vrp_7.value(), self.lineEdit_vrp_8.value(), self.lineEdit_vrp_6.value(), self.lineEdit_vrp_2.value(), self.lineEdit_av.value(), self.spinBox_apw.value(), 0, 1)
            
            self.time_data = []
            self.atr_data = []
            self.vent_data = []
            #Receive data
            if (self._conn.extract == 1):
                read_flag = 1
            else:
                read_flag = 0
            while (read_flag == 1):
                egram_data = self._conn.receive_data()
                read_flag = egram_data[2]
                
                #Send data to stop transmission
                if "V" in self.a_mode:
                    if "R" in self.a_mode:
                        self._conn.send_data(self.a_mode, self.spinBox_lrl.value(), self.lineEdit_vrp.value(), self.lineEdit_vrp_4.value(), self.lineEdit_vrp_7.value(), self.lineEdit_vrp_8.value(), self.lineEdit_vrp_6.value(), self.lineEdit_vrp_2.value(), self.lineEdit_va.value(), self.spinBox_vpw.value(), 1, 0)
                    else:
                        self._conn.send_data(self.a_mode, self.spinBox_lrl.value(), self.lineEdit_vrp.value(), self.lineEdit_vrp_4.value(), self.lineEdit_vrp_7.value(), self.lineEdit_vrp_8.value(), self.lineEdit_vrp_6.value(), self.lineEdit_vrp_2.value(), self.lineEdit_va.value(), self.spinBox_vpw.value(), 0, 0)
                else:
                    if "R" in self.a_mode:
                        self._conn.send_data(self.a_mode, self.spinBox_lrl.value(), self.lineEdit_arp.value(), self.lineEdit_vrp_4.value(), self.lineEdit_vrp_7.value(), self.lineEdit_vrp_8.value(), self.lineEdit_vrp_6.value(), self.lineEdit_vrp_2.value(), self.lineEdit_av.value(), self.spinBox_apw.value(), 1, 0)
                    else:
                        self._conn.send_data(self.a_mode, self.spinBox_lrl.value(), self.lineEdit_arp.value(), self.lineEdit_vrp_4.value(), self.lineEdit_vrp_7.value(), self.lineEdit_vrp_8.value(), self.lineEdit_vrp_6.value(), self.lineEdit_vrp_2.value(), self.lineEdit_av.value(), self.spinBox_apw.value(), 0, 0)
                
                egram_data = self._conn.receive_data()
                read_flag = egram_data[2]

            self.transmitting = False

    def on_a_thr_changed(self, hor):
        v = int(hor)
        if (v == 1):
            self.lineEdit_vrp_4.setSuffix(") V-Low")
        elif (v == 2):
            self.lineEdit_vrp_4.setSuffix(") Low")
        elif (v == 3):
            self.lineEdit_vrp_4.setSuffix(") Med-Low")
        elif (v == 4):
            self.lineEdit_vrp_4.setSuffix(") Med")
        elif (v == 5):
            self.lineEdit_vrp_4.setSuffix(") Med-High")
        elif (v == 6):
            self.lineEdit_vrp_4.setSuffix(") High")
        elif (v == 7):
            self.lineEdit_vrp_4.setSuffix(") V-High")

    def on_a_sens_changed(self, hor):
        v = float(hor)
        if (v > 0.74):
            if (v == 1.25):
                self.lineEdit_vrp_3.setValue(1)
            self.lineEdit_vrp_3.setSingleStep(0.5)
        else:
            self.lineEdit_vrp_3.setSingleStep(0.25)

    def on_v_sens_changed(self, hor):
        v = float(hor)
        if (v > 0.74):
            if (v == 1.25):
                self.lineEdit_vrp_3.setValue(1)
            self.lineEdit_vrp_3.setSingleStep(0.5)
        else:
            self.lineEdit_vrp_3.setSingleStep(0.25)

    def on_lrl_changed(self, hor):
        #a = Graph()
        #a.graphdata([1,2,3,4,5,6], [0,62,57,88,69,90], [60,62,57,88,69,90])#list(self.lineEdit_arp.value()), list(self.lineEdit_vrp.value()))
        v = int(hor)
        if (v < 49) and (v > 30):
            self.spinBox_lrl.setSingleStep(5)
        elif (v < 89) and (v > 49):
            self.spinBox_lrl.setSingleStep(1)
        elif (v < 175) and (v > 89):
            self.spinBox_lrl.setSingleStep(5)

    #def on_av_changed(self, hor):
    #    v = float(hor)
    #    if (v < 3.1) and (v > 0.5):
    #        self.lineEdit_av.setSingleStep(0.1)
    #    elif (v < 7.0) and (v > 3.1):
    #        self.lineEdit_av.setSingleStep(0.5)

    #def on_va_changed(self, hor):
    #    v = float(hor)
    #    if (v < 3.1) and (v > 0.5):
    #        self.lineEdit_va.setSingleStep(0.1)
    #    elif (v < 7.0) and (v > 3.1):
    #        self.lineEdit_va.setSingleStep(0.5)

    def on_vpw_changed(self, hor):
        v = float(hor)
        if (v > 0.05):
            self.spinBox_vpw.setSingleStep(0.1)
        elif (v < 0.11):
            self.spinBox_vpw.setSingleStep(0.05)

    def on_save_clicked(self):
        pass

    def save(self, mode):
        self.unique[mode] = []
        self.unique[mode].append(self.lineEdit_va.value())
        self.unique[mode].append(self.spinBox_vpw.value())
        self.unique[mode].append(self.spinBox_lrl.value())
        self.unique[mode].append(self.spinBox_url.value())
        self.unique[mode].append(self.lineEdit_av.value())
        self.unique[mode].append(self.spinBox_apw.value())
        self.unique[mode].append(self.lineEdit_vrp.value())
        self.unique[mode].append(self.lineEdit_arp.value())
        self.unique[mode].append(self.lineEdit_vrp_2.value())
        self.unique[mode].append(self.lineEdit_vrp_3.value())
        self.unique[mode].append(self.lineEdit_vrp_5.value())
        self.unique[mode].append(self.lineEdit_vrp_4.value())
        self.unique[mode].append(self.lineEdit_vrp_7.value())
        self.unique[mode].append(self.lineEdit_vrp_8.value())
        self.unique[mode].append(self.lineEdit_vrp_6.value())
    
    def load(self, mode):
        self.lineEdit_va.setValue(self.unique[mode][0])
        self.spinBox_vpw.setValue(self.unique[mode][1])
        self.spinBox_lrl.setValue(self.unique[mode][2])
        self.spinBox_url.setValue(self.unique[mode][3])
        self.lineEdit_av.setValue(self.unique[mode][4])
        self.spinBox_apw.setValue(self.unique[mode][5])
        self.lineEdit_vrp.setValue(self.unique[mode][6])
        self.lineEdit_arp.setValue(self.unique[mode][7])
        self.lineEdit_vrp_2.setValue(self.unique[mode][8])
        self.lineEdit_vrp_3.setValue(self.unique[mode][9])
        self.lineEdit_vrp_5.setValue(self.unique[mode][10])
        self.lineEdit_vrp_4.setValue(self.unique[mode][11])
        self.lineEdit_vrp_7.setValue(self.unique[mode][12])
        self.lineEdit_vrp_8.setValue(self.unique[mode][13])
        self.lineEdit_vrp_6.setValue(self.unique[mode][14])

    #def transmit_data(self):
    #    self._conn.send_data_to_pacemaker(self.get_params(self.a_mode))

    def pacing_mode_changed(self, e):
        if self.a_mode:
            self.save(self.a_mode)
            self.storage[self.username] = self.unique
            with open("data.json", "w") as f:
                f.write(json.dumps(self.storage))
        try:
            print(self.unique)
            self.load(self.sender().text())
        except:
            pass
        self.label_pacing_mode.setText(self.sender().text())
        self.a_mode = self.sender().text()
        self.export_ae.setVisible(True)
        self.export_ve.setVisible(True)
        self.export_ave.setVisible(True)
        if self.sender().text() == "VOO":
            self.frame_12.setVisible(False)
            self.frame_13.setVisible(False)
            self.frame_18.setVisible(True)
            self.frame_19.setVisible(False)
            self.frame_21.setVisible(False) # Maximum Sensor Rate
            self.frame_20.setVisible(False) # Atrial sens
            self.frame_23.setVisible(False) # Venticular sens
            self.frame_22.setVisible(False) # Activity Thr
            self.frame_25.setVisible(False) # Reaction time
            self.frame_26.setVisible(False) # Response factor
            self.frame_24.setVisible(False) # Recovery Time
            self.frame_11.setVisible(True)
            self.frame_10.setVisible(True)
            self.frame_17.setVisible(True)
            self.frame_16.setVisible(True)
        elif self.sender().text() == "AOO":
            self.frame_12.setVisible(True)
            self.frame_13.setVisible(True)
            self.frame_11.setVisible(True)
            self.frame_10.setVisible(True)
            self.frame_16.setVisible(False)
            self.frame_17.setVisible(False)
            self.frame_18.setVisible(False)
            self.frame_19.setVisible(True)
            self.frame_21.setVisible(False) # Maximum Sensor Rate
            self.frame_20.setVisible(False) # Atrial sens
            self.frame_23.setVisible(False) # Venticular sens
            self.frame_22.setVisible(False) # Activity Thr
            self.frame_25.setVisible(False) # Reaction time
            self.frame_26.setVisible(False) # Response factor
            self.frame_24.setVisible(False) # Recovery Time
        elif self.sender().text() == "AAI":
            self.frame_16.setVisible(False)
            self.frame_17.setVisible(False)
            self.frame_18.setVisible(False)
            self.frame_21.setVisible(False) # Maximum Sensor Rate
            self.frame_20.setVisible(False) # Atrial sens
            self.frame_23.setVisible(False) # Venticular sens
            self.frame_22.setVisible(False) # Activity Thr
            self.frame_25.setVisible(False) # Reaction time
            self.frame_26.setVisible(False) # Response factor
            self.frame_24.setVisible(False) # Recovery Time
            self.frame_12.setVisible(True)
            self.frame_13.setVisible(True)
            self.frame_19.setVisible(True)
            self.frame_11.setVisible(True)
            self.frame_10.setVisible(True)
        elif self.sender().text() == "VVI":
            self.frame_16.setVisible(True)
            self.frame_17.setVisible(True)
            self.frame_18.setVisible(True)
            self.frame_12.setVisible(False)
            self.frame_13.setVisible(False)
            self.frame_19.setVisible(False)
            self.frame_21.setVisible(False) # Maximum Sensor Rate
            self.frame_20.setVisible(False) # Atrial sens
            self.frame_23.setVisible(False) # Venticular sens
            self.frame_22.setVisible(False) # Activity Thr
            self.frame_25.setVisible(False) # Reaction time
            self.frame_26.setVisible(False) # Response factor
            self.frame_24.setVisible(False) # Recovery Time
            self.frame_11.setVisible(True)
            self.frame_10.setVisible(True)
        elif self.sender().text() == "AOOR":
            self.frame_21.setVisible(True) # Maximum Sensor Rate
            self.frame_20.setVisible(False) # Atrial sens
            self.frame_23.setVisible(False) # Venticular sens
            self.frame_22.setVisible(True) # Activity Thr
            self.frame_25.setVisible(True) # Reaction time
            self.frame_26.setVisible(True) # Response factor
            self.frame_24.setVisible(True) # Recovery Time
            self.frame_11.setVisible(True)
            self.frame_10.setVisible(True)
            self.frame_12.setVisible(True)
            self.frame_13.setVisible(True)
            self.frame_16.setVisible(False)
            self.frame_17.setVisible(False)
            self.frame_18.setVisible(False)
            self.frame_19.setVisible(True)
        elif self.sender().text() == "VOOR":
            self.frame_21.setVisible(True) # Maximum Sensor Rate
            self.frame_20.setVisible(False) # Atrial sens
            self.frame_23.setVisible(False) # Venticular sens
            self.frame_22.setVisible(True) # Activity Thr
            self.frame_25.setVisible(True) # Reaction time
            self.frame_26.setVisible(True) # Response factor
            self.frame_24.setVisible(True) # Recovery Time
            self.frame_11.setVisible(True)
            self.frame_10.setVisible(True)
            self.frame_16.setVisible(True)
            self.frame_17.setVisible(True)
            self.frame_12.setVisible(False)
            self.frame_13.setVisible(False)
            self.frame_19.setVisible(False)
            self.frame_18.setVisible(True)
        elif self.sender().text() == "AAIR":
            self.frame_21.setVisible(True) # Maximum Sensor Rate
            self.frame_20.setVisible(True) # Atrial sens
            self.frame_23.setVisible(False) # Venticular sens
            self.frame_22.setVisible(True) # Activity Thr
            self.frame_25.setVisible(True) # Reaction time
            self.frame_26.setVisible(True) # Response factor
            self.frame_24.setVisible(True) # Recovery Time
            self.frame_11.setVisible(True)
            self.frame_10.setVisible(True)
            self.frame_12.setVisible(True)
            self.frame_13.setVisible(True)
            self.frame_16.setVisible(False)
            self.frame_17.setVisible(False)
            self.frame_18.setVisible(False)
            self.frame_19.setVisible(True)
        elif self.sender().text() == "VVIR":
            self.frame_21.setVisible(True) # Maximum Sensor Rate
            self.frame_20.setVisible(False) # Atrial sens
            self.frame_23.setVisible(True) # Venticular sens
            self.frame_22.setVisible(True) # Activity Thr
            self.frame_25.setVisible(True) # Reaction time
            self.frame_26.setVisible(True) # Response factor
            self.frame_24.setVisible(True) # Recovery Time
            self.frame_11.setVisible(True)
            self.frame_10.setVisible(True)
            self.frame_16.setVisible(True)
            self.frame_17.setVisible(True)
            self.frame_12.setVisible(False)
            self.frame_13.setVisible(False)
            self.frame_19.setVisible(False)
            self.frame_18.setVisible(True)
        else:
            print("Error!")



    def get_params(self, pace_mode):
        typed_params = {"Pacing Mode": self._pacing_modes[pace_mode]}
        ups = {
            "Lower Rate Limit":self.spinBox_lrl.value(),
            "Upper Rate Limit":self.spinBox_url.value(),
            "Maximum Sensor Rate":self.lineEdit_vrp_2.value(),
            "Fixed AV Delay":0,
            "Atrial Amplitude":self.lineEdit_av.value(),
            "Atrial Pulse Width":self.spinBox_apw.value(),
            "Atrial Sensitivity":self.lineEdit_vrp_3.value(),
            "Ventricular Amplitude" : self.lineEdit_va.value(),
            "Ventricular Pulse Width" : self.spinBox_vpw.value(),
            "Ventricular Sensitivity":self.lineEdit_vrp_5.value(),
            "ARP":self.lineEdit_arp.value(),
            "VRP":self.lineEdit_vrp.value(),
            "PVARP":0,
            "Activity Threshold":self.lineEdit_vrp_4.value(),
            "Reaction Time":self.lineEdit_vrp_7.value(),
            "Response Factor":self.lineEdit_vrp_8.value(),
            "Recovery Time":self.lineEdit_vrp_6.value()}
        print("lala", ups)
        for key, value in ups.items():
            try:
                typed_params[key] = int(value)
            except:
                try:
                    typed_params[key] = int(float(value) * 20)
                except:
                    typed_params[key] = self._act_thresh.index(value) + 1
        return typed_params

    # click event of logout button
    def onclick_btn_logout(self):
        self.hide()
        self.parent.show()
