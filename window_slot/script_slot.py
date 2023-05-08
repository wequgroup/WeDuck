import os
import time
from PySide2.QtWidgets import QFileDialog

from utils.action_record import ActionRecord


class Script:
    def __init__(self, win):
        self.win = win
        self.script_name = str(int(time.time()))

    def record_script(self):
        self.win.log("正在录制脚本...")
        self.win.ScriptButton.setText("正在录制脚本...")
        action = ActionRecord("{}.txt".format(self.script_name))
        action.run()
        self.win.log("脚本录制成功，名称为：" + self.script_name)
        self.win.ScriptButton.setText("录制新脚本")
        self.win.show()
        self.win.ScriptNameEdit.setText(self.script_name)

    def show_script(self):
        script_path = os.path.join(os.getcwd(), "script")
        script_dialog = QFileDialog()
        script_dialog.getOpenFileNames(self.win, "微趣鸭录制的脚本", script_path)
        self.win.log("打开录制脚本路径：" + script_path)
