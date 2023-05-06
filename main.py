import os
import sys

os.environ['QT_MAC_WANTS_LAYER'] = '1'

from PySide2.QtWidgets import QApplication
from window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
