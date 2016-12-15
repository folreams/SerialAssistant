# -*---------coding utf8----------------*-

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
    sys.exit(app.exec_())
  