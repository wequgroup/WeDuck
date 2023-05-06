import _thread
import os
import time

from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import QColor, QIcon
from PySide2.QtWidgets import QMainWindow, QSystemTrayIcon, \
    QAction, QMenu, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QDialog, QWidget

from ui import Ui_MainWindow
from utils import config
from window_slot.login_slot import Login
from window_slot.script_slot import Script


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # 日志颜色
        c = QColor(112, 128, 105)
        self.LogList.setTextColor(c)
        self.device = Login(self)
        self.script = Script(self)
        self.icon = QIcon(os.path.join(os.getcwd(), "icon.png"))
        self.init_app()
        self.init_connect()
        self.dialog = Dialog()

    def log(self, msg):
        log_time = time.strftime("%m-%d %H:%M", time.localtime())
        self.LogList.append(log_time + " - " + msg)

    def init_app(self):
        # 获取版本号
        version = config.get("app", "version")
        self.setWindowTitle("微趣鸭 v" + version)
        self.setWindowIcon(self.icon)
        self.create_tray_icon()
        # 获取设备账号密码
        device_id = config.get("device", "id")
        device_password = config.get("device", "password")
        auto_online = config.get("device", "auto_online")
        if len(device_password) == 6 and len(device_id) == 8:
            self.DeviceIDEdit.setText(device_id)
            self.DevicePassEdit.setText(device_password)

        if auto_online == "yes":
            self.AutoOnlineCheckBox.setChecked(True)
            self.device.login()

    def init_connect(self):
        # 连接服务器
        self.LoginButton.clicked.connect(self.login_btn_click)
        # 断开服务器
        self.LogoutButton.clicked.connect(self.logout_btn_click)
        # 录制脚本
        self.ScriptButton.clicked.connect(self.script_btn_click)
        # 查看录制脚本
        self.MyScriptButton.clicked.connect(self.my_script_btn_click)

    # 创建托盘图标
    def create_tray_icon(self):
        restore_app = QAction('显示应用', self, triggered=self.show_window)
        exit_app = QAction('退出应用', self, triggered=QApplication.instance().quit)

        menu = QMenu(self)
        menu.addAction(restore_app)
        menu.addAction(exit_app)
        tray = QSystemTrayIcon(self)
        tray.setIcon(self.icon)
        tray.setContextMenu(menu)
        tray.show()

    @Slot()
    def login_btn_click(self):
        _thread.start_new_thread(self.device.login, ())

    @Slot()
    def logout_btn_click(self):
        self.device.logout()

    @Slot()
    def script_btn_click(self):
        self.hide()
        self.dialog.show()
        # _thread.start_new_thread(self.script.record_script, ())

    @Slot()
    def my_script_btn_click(self):
        self.script.show_script()

    def show_window(self):
        if self.isVisible() is False:
            self.show()
        else:
            self.showNormal()


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.desktop = QApplication.desktop()
        vbox = QVBoxLayout()  # 纵向布局
        hbox = QHBoxLayout()  # 横向布局
        panel = QLabel()
        panel.setText("按下 Esc 键结束录制")
        self.resize(250, 70)
        self.setWindowTitle("正在录制中")
        vbox.addWidget(panel)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.move(int(self.desktop.width() / 2.89), 0)
        self.setWindowModality(Qt.ApplicationModal)
