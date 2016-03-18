import sqlite3
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import sys
from PyQt4 import QtCore, QtGui, uic

#import ui file
qtCreatorFile = "CraneCapacityLookUp.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

#create ui class
class myApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.findCapacity)
    
    def findCapacity(self):
        def queryDb(column, crane, cwt):
            conn = sqlite3.connect('crane.db')        
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute("SELECT {} FROM {} WHERE counterweight = {}".format(column, crane, cwt))
            x=[]
            for row in c:
                x.append(row[0])
            return x
        crane = 'DemagAc435' # self.craneInput.text() #'DemagAc435' 
        BoomType ='SH' #self.BoomTypeInput.text() #'SH'
        cwt =59500#int(self.CounterweightInput.text()) # 97000
        outrigger ='Full'#self.OutriggerInput.text() #'Full'
        Boomlen =164 #int(self.BoomLength.text()) #164
        radius =51#int(self.RadiusInput.text()) #26
        #database lookup
        dbin = (BoomType,cwt,outrigger,Boomlen,radius)
        conn = sqlite3.connect('crane.db')
        c = conn.cursor()
        c.execute("SELECT Capacity FROM %s WHERE BoomType == ? and Counterweight == ? and Outrigger == ? and Boomlen == ? and Radius >= ?" %crane, dbin)
        capacity = str(c.fetchone()[0])
        #get data for plot
        x = queryDb('Radius', crane, cwt)
        y = queryDb('Capacity', crane, cwt)
        #plot data in gui window
        #mplw.MatplotlibWidget().getFigure().add_subplot(111)
        #mplw.MatplotlibWidget().plot(x,y)
        #mplw.MatplotlibWidget().draw()
        self.textBrowser.setText(capacity)
        

            
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    window = myApp()
    window.show()
    sys.exit(app.exec_())
