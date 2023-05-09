import argparse
import os
import sys
sys.stdout = open(os.devnull, 'w')
if sys.platform == "darwin":
    os.environ['QT_MAC_WANTS_LAYER'] = '1'
from PySide2.QtCore import QLockFile
from utils.get_root_path import root_path
from PySide2.QtWidgets import QApplication, QMessageBox
from window import MainWindow

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mini", dest="if_mini", help="is mini?")
    args = parser.parse_args()
    if_mini = args.if_mini
    app = QApplication(sys.argv)
    lockFile = QLockFile(os.path.join(root_path, "WeDuck.app.lock"))
    if lockFile.tryLock(2000):
        win = MainWindow()
        win.setMinimumSize(407, 391)
        win.setMaximumSize(407, 391)
        if if_mini:
            win.hide()
        else:
            win.show()
    else:
        msg_box = QMessageBox()
        msg_box.setWindowTitle("提示")
        msg_box.setText("微趣鸭已在运行!")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.addButton("确定", QMessageBox.YesRole)
        msg_box.exec()
        sys.exit(-1)
    sys.exit(app.exec_())
