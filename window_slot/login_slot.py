import requests
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QMessageBox

import g
from utils import config
from utils.mqtt import MQTT


class Login:

    def __init__(self, window: QMainWindow):
        self.win: QMainWindow = window
        self.device_id: str = ""
        self.device_password: str = ""
        self.msg: QMessageBox = QMessageBox()

    def init_input(self):
        self.win.LoginButton.setDisabled(False)
        self.win.LoginButton.setText("连接服务器")

    def run(self):
        self.win.log("正在校验设备信息...")
        self.win.LoginButton.setText("连接中...")
        self.win.LoginButton.setDisabled(True)
        self.device_id: str = self.win.DeviceIDEdit.text()
        self.device_password: str = self.win.DevicePassEdit.text()
        if self.check_device():
            self.win.log("设备信息校验成功！")
            mqtt = MQTT(self.device_id, self.device_password, win=self.win)
            mqtt.start()

    def logout(self):
        g.STOP_MQ = True
        self.win.LoginButton.setText("连接服务器")
        self.win.LoginButton.setDisabled(False)
        self.win.LogoutButton.setEnabled(False)
        self.win.DeviceIDEdit.setEnabled(True)
        self.win.DevicePassEdit.setEnabled(True)

    def check_device(self) -> bool:
        if len(self.device_id) != 8 or len(self.device_password) != 6:
            err_msg: str = "请输入正确的设备编号或密码"
            self.win.log(err_msg)
            self.msg.warning(self.win, "提示", err_msg)
            self.init_input()
            return False
        try:
            res: requests = requests.get("https://api.wequ.net/app/duck/device/client/{}/{}".
                                         format(self.device_id, self.device_password), timeout=5)
            if res.json().get("data") is None:
                err_msg: str = "未查询到{}设备信息".format(self.device_id)
                self.win.log(err_msg)
                self.msg.warning(self.win, "提示", err_msg)
                self.init_input()
                return False

            config.set("device", "id", self.device_id)
            config.set("device", "password", self.device_password)
            if self.win.AutoOnlineCheckBox.isChecked():
                config.set("device", "auto_online", "yes")
            else:
                config.set("device", "auto_online", "off")
            return True
        except requests.exceptions.Timeout:
            err_msg: str = "网络超时，请检查网络"
            self.win.log(err_msg)
            self.msg.warning(self.win, "提示", err_msg)
            self.init_input()
            return False
