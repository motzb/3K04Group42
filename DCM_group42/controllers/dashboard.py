from enum import unique
from functools import partial

from PyQt5.QtWidgets import QMainWindow, QRadioButton

from views.dashboard import Ui_Dashboard

import json

# Dashboard controller class that will handle all the events of the widgets in the dashboard view
class Dashboard(QMainWindow, Ui_Dashboard):
    def __init__(self, parent):
        super(Dashboard, self).__init__()
        self.setupUi(self)
        self.username = None
        self.parent = parent
        # \/ This is a dict that stores unique values for each mode
        self.unique = {}
        try:
            with open("data.json", "r") as f:
                self.unique = json.loads(f.read())
        except:
            print("File not exist")
        # \/ This is a variable in which the mode that was just turned on is written, this is necessary to save
        self.a_mode = None

    # to initialize the dashboard view after login for a particular user
    def init(self, username):
        self.username = username
        self.label_welcome.setText("Hi, {}".format(self.username))

    # function overriding, setupUi function setup call for widgets
    def setupUi(self, Dashboard):
        Ui_Dashboard.setupUi(self, Dashboard)

        # \/ This is the connection of the function when the value of the field changes
        self.spinBox_lrl.valueChanged.connect(self.on_lrl_changed)
        self.lineEdit_va.valueChanged.connect(self.on_va_changed)
        self.lineEdit_av.valueChanged.connect(self.on_va_changed)
        self.spinBox_vpw.valueChanged.connect(self.on_vpw_changed)
        self.spinBox_apw.valueChanged.connect(self.on_vpw_changed)
        # /\ This is the connection of the function when the value of the field changes

        # click handlers of the buttons in the ui
        self.pushButton_save.clicked.connect(self.on_save_clicked)
        self.btn_logout.clicked.connect(self.on_logout_clicked)

        # I don't know how it works, I've never used it
        # \/ But it's definitely a loop that connects each mode selection to a function
        for i, pacing_mode in enumerate(filter(lambda x: isinstance(x, QRadioButton),
                                               self.frame_pacing_modes.children())):
            pacing_mode.toggled.connect(self.on_pacing_mode_changed)
        
        # \/ Making all fields invisible so that there are no display problems when switching modes
        self.frame_12.setVisible(False)
        self.frame_13.setVisible(False)
        self.frame_18.setVisible(False)
        self.frame_19.setVisible(False)
        self.frame_11.setVisible(False)
        self.frame_10.setVisible(False)
        self.frame_17.setVisible(False)
        self.frame_16.setVisible(False)
        #######

    # Function that is activated when the lower rate limit changes value
    def on_lrl_changed(self, hor):
        v = int(hor)
        # \/ Checking field values and changing the increment
        if (v < 49) and (v > 30):
            self.spinBox_lrl.setSingleStep(5)
        elif (v < 89) and (v > 49):
            self.spinBox_lrl.setSingleStep(1)
        elif (v < 175) and (v > 89):
            self.spinBox_lrl.setSingleStep(5)

    # Function that is activated when the venticular amplitude and atrial amplitude changes value
    def on_va_changed(self, hor):
        v = float(hor)
        # \/ Checking field values and changing the increment
        if (v < 3.1) and (v > 0.5):
            self.lineEdit_va.setSingleStep(0.1)
        elif (v < 7.0) and (v > 3.1):
            self.lineEdit_va.setSingleStep(0.5)

    # Function that is activated when the venticular pulse witdh and atrial pulse width changes value
    def on_vpw_changed(self, hor):
        v = float(hor)
        # \/ Checking field values and changing the increment
        if (v > 0.05):
            self.spinBox_vpw.setSingleStep(0.1)
        elif (v < 0.11):
            self.spinBox_vpw.setSingleStep(0.05)

    # An empty function for the save button, which should have had an implementation of saving on click
    def on_save_clicked(self):
        print("Saved!")
        with open("data.json", "w") as f:
            f.write(json.dumps(self.unique))
    
    def closeEvent(self, event):
        print("Saved!")
        with open("data.json", "w") as f:
            f.write(json.dumps(self.unique))
        event.accept() # let the window close
        
    
    # Save function
    def save(self, mode):
        # Initialize a list variable for the specified mode
        self.unique[mode] = []
        # \/ Adding a value from fields to a list
        self.unique[mode].append(self.lineEdit_va.value())
        self.unique[mode].append(self.spinBox_vpw.value())
        self.unique[mode].append(self.spinBox_lrl.value())
        self.unique[mode].append(self.spinBox_url.value())
        self.unique[mode].append(self.lineEdit_av.value())
        self.unique[mode].append(self.spinBox_apw.value())
        self.unique[mode].append(self.lineEdit_vrp.value())
        self.unique[mode].append(self.lineEdit_arp.value())
        ########

    # Load function
    def load(self, mode):
        # \/ Setting field values from a list of unique values
        self.lineEdit_va.setValue(self.unique[mode][0])
        self.spinBox_vpw.setValue(self.unique[mode][1])
        self.spinBox_lrl.setValue(self.unique[mode][2])
        self.spinBox_url.setValue(self.unique[mode][3])
        self.lineEdit_av.setValue(self.unique[mode][4])
        self.spinBox_apw.setValue(self.unique[mode][5])
        self.lineEdit_vrp.setValue(self.unique[mode][6])
        self.lineEdit_arp.setValue(self.unique[mode][7])
        #########

    def on_pacing_mode_changed(self, e):
        # Checking if a mode is enabled
        if self.a_mode:
            self.save(self.a_mode)
            # \/ Attempt to load the fields, if they are saved then the load function is executed, if not then the function is skipped
        try:
            self.load(self.sender().text())
        except:
            pass
            #######
        # Setting the mode name in the text field
        self.label_pacing_mode.setText(self.sender().text())
        # Getting the current mode and writing to a variable
        self.a_mode = self.sender().text()

        """
        The names of the frames in which the elements are located

        lineEdit_va frame_16
        spinBox_vpw frame_17

        spinBox_lrl frame_11
        spinBox_url frame_10

        lineEdit_av frame_12
        spinBox_apw frame_13

        lineEdit_vrp frame_18
        lineEdit_arp frame_19
        """

        # Mode check
        if self.sender().text() == "VOO":
            # Setting fields visible / invisible depending on the mode
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
    # Clicking the logout button hides the current window and opens the parent window
    def on_logout_clicked(self):
        self.hide()
        self.parent.show()
