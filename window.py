import _thread
import os
import sys
import time

from PySide2.QtCore import Slot
from PySide2.QtGui import QColor, QIcon
from PySide2.QtWidgets import QMainWindow, QSystemTrayIcon, \
    QAction, QMenu, QApplication

from ui import Ui_MainWindow
from utils import config
from utils.get_root_path import root_path
from window_slot.login_slot import Login
from window_slot.script_slot import Script
from window_slot.update_slot import Update


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # 日志颜色
        c = QColor(112, 128, 105)
        self.LogList.setTextColor(c)
        self.version = config.get("app", "version")
        self.os = sys.platform
        self.device = Login(self)
        self.script = Script(self)
        if sys.platform == "darwin":
            self.icon = QIcon(os.path.join(root_path, "icon.icns"))
        else:
            self.icon = QIcon(os.path.join(root_path, "icon.png"))
        self.init_app()
        self.init_connect()

    def log(self, msg):
        log_time = time.strftime("%m-%d %H:%M", time.localtime())
        self.LogList.append(log_time + " - " + msg)

    def init_app(self):
        # 获取版本号
        self.VersionLabel.setText("当前版本：V" + self.version)
        self.OS_Label.setText("当前系统：" + self.os)
        self.setWindowTitle("微趣鸭 v" + self.version)
        self.setWindowIcon(self.icon)
        self.create_tray_icon()
        # 获取设备账号密码
        device_id = config.get("device", "id")
        device_password = config.get("device", "password")
        auto_online = config.get("device", "auto_online")
        # 设置mac提示
        if sys.platform == "darwin":
            self.MacTips.setText("Mac系统用户请在系统设置-安全与隐私-辅助功能-添加应用<br>然后在输入监控-添加应用，否则无法录制脚本")
        if len(device_password) == 6 and len(device_id) == 8:
            self.DeviceIDEdit.setText(device_id)
            self.DevicePassEdit.setText(device_password)
        if auto_online == "yes":
            self.AutoOnlineCheckBox.setChecked(True)
            self.login_btn_click()

    def init_connect(self):
        # 连接服务器
        self.LoginButton.clicked.connect(self.login_btn_click)
        # 断开服务器
        self.LogoutButton.clicked.connect(self.logout_btn_click)
        # 录制脚本
        self.ScriptButton.clicked.connect(self.script_btn_click)
        # 查看录制脚本
        self.MyScriptButton.clicked.connect(self.my_script_btn_click)
        # 更新版本
        self.UpdateButton.clicked.connect(self.update_btn_click)

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
        up = Update(self)
        if up.update(self.version, self.os) is not True:
            self.device.run()
        else:
            self.LoginButton.setDisabled(True)

    @Slot()
    def logout_btn_click(self):
        self.device.logout()

    @Slot()
    def script_btn_click(self):
        self.hide()
        _thread.start_new_thread(self.script.record_script, ())

    @Slot()
    def my_script_btn_click(self):
        self.script.show_script()

    @Slot()
    def update_btn_click(self):
        up = Update(self)
        up.update(self.version, self.os)

    def show_window(self):
        if self.isVisible() is False:
            self.show()
        else:
            self.showNormal()

    def closeEvent(self, event):
        """后台运行"""
        self.hide()
        event.ignore()
