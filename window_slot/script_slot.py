import os
import time
from PySide2.QtWidgets import QFileDialog
from utils.get_root_path import home_path
from utils.action_record import ActionRecord


class Script:
    def __init__(self, win):
        self.win = win

    def record_script(self):
        script_name = str(int(time.time()))
        self.win.log("正在录制脚本...")
        self.win.ScriptButton.setText("正在录制脚本...")
        action = ActionRecord("{}.txt".format(script_name))
        action.run()
        self.win.log("脚本录制成功，名称为：" + script_name)
        self.win.ScriptButton.setText("录制新脚本")
        self.win.show()
        self.win.ScriptNameEdit.setText(script_name)

    def show_script(self):
        script_path = os.path.join(home_path, "script")
        script_dialog = QFileDialog()
        script_dialog.getOpenFileNames(self.win, "微趣鸭录制的脚本", script_path)
        self.win.log("打开录制脚本路径：" + script_path)
