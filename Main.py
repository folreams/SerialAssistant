#----coding utf8-----------------------------
__Version__ = "V1.0"
__Author__  = "DayuZhang"
__email__ = "folreams@gmail.com"

import sys
from PyQt4 import QtGui
from MainWindow import MainWindows
if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    app.setOrganizationName("Allsine")
    app.setOrganizationDomain("www.allsine.com")
    app.setApplicationName("Serial Assistant")
    app.setWindowIcon(QtGui.QIcon(":/icon.png"))
    win = MainWindows()
    win.show()
    app.exec_()
    sys.exit(app.exec_())
  