from utils.action_play import ActionPlay
from utils.shell_play import ShellPlay
import os
import json
script_path = os.path.join(os.getcwd(), "script")


class Play:
    def __init__(self, msg, win):
        self.shellType = msg["shellType"]
        self.shellContent = msg["shellContent"]
        self.win = win

    def run(self):
        if self.shellType == 0:
            self.shell()
        if self.shellType == 1:
            self.action()

    def shell(self):
        self.win.log("开始执行脚本命令:" + self.shellContent)
        s = ShellPlay(self.shellContent)
        s.run()
        self.win.log("脚本命令执行结束")

    def action(self):
        self.win.log("开始执行操作回放:" + self.shellContent)
        with open(os.path.join(script_path, self.shellContent + ".txt"), encoding="utf-8") as s:
            script = s.read()
        self.win.hide()
        a = ActionPlay(script)
        a.run()
        self.win.log("操作回放执行结束")
