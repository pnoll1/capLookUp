import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import sys
from PyQt4 import QtCore, QtGui, uic
#import CraneCapacityLookUp #ui file

#ui file
qtCreatorFile = "CraneCapacityLookUp.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class myApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.findCapacity)
        
    def findCapacity(self):
        crane = self.craneInput.text() #'DemagAc435' 
        BoomType = self.BoomTypeInput.text() #'SH'
        cwt =int(self.CounterweightInput.text()) # 97000
        outrigger =self.OutriggerInput.text() #'Full'
        Boomlen = int(self.BoomLength.text()) #164
        radius =int(self.RadiusInput.text()) #26
        #database lookup
        dbin = (BoomType,cwt,outrigger,Boomlen,radius)
        conn = sqlite3.connect('crane.db')
        c = conn.cursor()
        c.execute("SELECT Capacity FROM %s WHERE BoomType == ? and Counterweight == ? and Outrigger == ? and Boomlen == ? and Radius > ?" %crane, dbin)
        capacity = str(c.fetchone()[0])
        self.textBrowser.setText(capacity)
        #return capacity

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    window = myApp()
    window.show()
    sys.exit(app.exec_())
