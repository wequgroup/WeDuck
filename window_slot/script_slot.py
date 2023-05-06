import os
import subprocess
import sys

from utils.action_record import ActionRecord


class Script:
    def __init__(self, win, script_name=""):
        self.win = win
        self.script_name = script_name

    def record_script(self):
        self.win.log("正在录制脚本...")
        self.win.ScriptButton.setText("正在录制脚本...")
        ActionRecord("test.txt").run()
        self.win.log("脚本录制成功，名称为：" + self.script_name)
        self.win.ScriptButton.setText("录制新脚本")

    def show_script(self):
        script_path = os.path.join(os.getcwd(), "script")
        self.win.log("打开录制脚本路径：" + script_path)
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, script_path])
