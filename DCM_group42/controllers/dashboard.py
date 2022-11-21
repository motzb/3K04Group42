from functools import partial

from PyQt5.QtWidgets import QMainWindow, QRadioButton

import json

from views.dashboard import Ui_Dashboard


# Dashboard controller class that will handle all the events of the widgets in the dashboard view
class Dashboard(QMainWindow, Ui_Dashboard):
    def __init__(self, parent):
        super(Dashboard, self).__init__()
        self.setupUi(self)
        self.username = None
        self.parent = parent
        self.unique = {}
        self.storage = {}
        self.a_mode = None

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
            self.frame_18.setVisible(False)
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
            self.frame_19.setVisible(False)
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
            self.frame_19.setVisible(False)
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
            self.frame_19.setVisible(False)
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
        else:
            print("Error!")

    # click event of logout button
    def onclick_btn_logout(self):
        self.hide()
        self.parent.show()
