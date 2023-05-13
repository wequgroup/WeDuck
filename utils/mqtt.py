import _thread
import json
import time
from threading import Event

import paho.mqtt.client as mqtt
from PySide2.QtWidgets import QMainWindow

import g
from utils.base_play import Play


class MQTT:

    def __init__(self, user_name: str, password: str,
                 host: str = "mqtt-hw.wequ.net", port: int = 1883, win: QMainWindow = None):
        self.client = mqtt.Client(client_id=user_name, clean_session=False)
        self.client.keep_alive = 60
        self.client.username_pw_set(username=user_name, password=password)
        self.host = host
        self.port = port
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.username = user_name
        self.win: QMainWindow = win
        self.event = Event()

    def on_disconnect(self, rc, a, b):
        while rc != 0 and rc != 5:
            try:
                self.win.log("正在重连服务器中...")
                rc = self.client.reconnect()
                self.client.subscribe(topic=str("duck/" + self.username), qos=0)
            except:
                self.win.log("重连服务器失败，15秒后重试")
                time.sleep(15)

    def on_connect(self, client, userdata, rc, msg):
        if msg == 5:
            self.win.log("设备登录失败，请检查设备信息")
            self.close_mq()
        if msg == 0:
            self.win.LoginButton.setText("已连接到服务端")
            self.win.LogoutButton.setEnabled(True)
            self.win.DeviceIDEdit.setEnabled(False)
            self.win.DevicePassEdit.setEnabled(False)
            self.win.log("设备连接服务端成功")

    def on_message(self, client, userdata, rc):
        msg = rc.payload
        try:
            params = json.loads(msg)
            if type(params) is not int:
                shell_play = Play(params, self.win)
                _thread.start_new_thread(shell_play.run, ())
        except Exception as e:
            self.win.log("指令已下发但未执行：" + str(e))
            return False
        return True

    def ping(self):
        """40秒发个心跳"""
        while True:
            if g.STOP_MQ is True:
                break
            else:
                self.client.publish(topic=str("duck/" + self.username), payload="1", qos=0)
                self.event.wait(50)

    def start(self):
        # 连接到MQTT服务器
        self.win.log("连接服务器中...")
        _thread.start_new_thread(self.stop_mq, ())
        rc = self.client.connect(self.host, self.port)
        if rc == 0:
            self.client.subscribe(topic=str("duck/" + self.username), qos=0)
            self.client.loop_start()
            _thread.start_new_thread(self.ping, ())
        else:
            self.win.log("连接服务器失败")
            pass

    def stop_mq(self):
        while True:
            if g.STOP_MQ:
                self.close_mq()
                break
            time.sleep(0.15)

    def close_mq(self):
        g.STOP_MQ = True
        self.event.set()
        self.client.disconnect()
        self.client.loop_stop()
        self.win.log("设备已下线！")
        time.sleep(0.1)
        g.STOP_MQ = False
