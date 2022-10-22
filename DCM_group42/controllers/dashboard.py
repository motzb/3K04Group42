from functools import partial

from PyQt5.QtWidgets import QMainWindow, QRadioButton

from views.dashboard import Ui_Dashboard


# Dashboard controller class that will handle all the events of the widgets in the dashboard view
class Dashboard(QMainWindow, Ui_Dashboard):
    def __init__(self, parent):
        super(Dashboard, self).__init__()
        self.setupUi(self)
        self.username = None
        self.parent = parent
        self.unique = {}
        self.a_mode = None

    # to initialize the dashboard view after login for a particular user
    def init(self, username):
        self.username = username
        self.label_welcome.setText("Hi, {}".format(self.username))

    # function overriding, setupUi function setup call for widgets
    def setupUi(self, Dashboard):
        Ui_Dashboard.setupUi(self, Dashboard)

        # click handlers of the buttons in the ui
        self.spinBox_lrl.valueChanged.connect(self.on_lrl_changed)
        self.lineEdit_va.valueChanged.connect(self.on_va_changed)
        self.lineEdit_av.valueChanged.connect(self.on_va_changed)
        self.spinBox_vpw.valueChanged.connect(self.on_vpw_changed)
        self.spinBox_apw.valueChanged.connect(self.on_vpw_changed)
        self.pushButton_save.clicked.connect(self.on_save_clicked)
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

    def on_lrl_changed(self, hor):
        v = int(hor)
        if (v < 49) and (v > 30):
            self.spinBox_lrl.setSingleStep(5)
        elif (v < 89) and (v > 49):
            self.spinBox_lrl.setSingleStep(1)
        elif (v < 175) and (v > 89):
            self.spinBox_lrl.setSingleStep(5)

    def on_va_changed(self, hor):
        v = float(hor)
        if (v < 3.1) and (v > 0.5):
            self.lineEdit_va.setSingleStep(0.1)
        elif (v < 7.0) and (v > 3.1):
            self.lineEdit_va.setSingleStep(0.5)

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
    
    def load(self, mode):
        self.lineEdit_va.setValue(self.unique[mode][0])
        self.spinBox_vpw.setValue(self.unique[mode][1])
        self.spinBox_lrl.setValue(self.unique[mode][2])
        self.spinBox_url.setValue(self.unique[mode][3])
        self.lineEdit_av.setValue(self.unique[mode][4])
        self.spinBox_apw.setValue(self.unique[mode][5])
        self.lineEdit_vrp.setValue(self.unique[mode][6])
        self.lineEdit_arp.setValue(self.unique[mode][7])

    def pacing_mode_changed(self, e):
        if self.a_mode:
            self.save(self.a_mode)
            try:
                self.load(self.sender().text())
            except:
                pass
        self.label_pacing_mode.setText(self.sender().text())
        self.a_mode = self.sender().text()
        if self.sender().text() == "VOO":
            self.frame_12.setVisible(False)
            self.frame_13.setVisible(False)
            self.frame_18.setVisible(False)
            self.frame_19.setVisible(False)
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
        elif self.sender().text() == "AAI":
            self.frame_16.setVisible(False)
            self.frame_17.setVisible(False)
            self.frame_18.setVisible(False)
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
            self.frame_11.setVisible(True)
            self.frame_10.setVisible(True)
        else:
            print("Error!")

    # click event of logout button
    def onclick_btn_logout(self):
        self.hide()
        self.parent.show()
