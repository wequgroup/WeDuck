import json
import os
import re

import requests
from PySide2.QtWidgets import QMessageBox

root_path = os.getcwd()


class Update:
    def __init__(self, win):
        self.win = win

    def update(self, version, os):
        res = requests.get("https://api.wequ.net/app/duck/post/4").json()
        app_info = json.loads(res["data"]["value"])
        app_os_info = app_info[os]
        if int(version) < int(app_os_info["version"]):
            update_info = "有新版本[{}]: {}<br><br>更新内容<br>{}" \
                .format("强制更新" if app_info["update_type"] == 0 else "选择更新", app_os_info["version"],
                        app_info["update_content"])
            msg_box = QMessageBox(QMessageBox.Information, "升级提示", update_info, QMessageBox.NoButton, self.win)
            msg_box.addButton(QMessageBox.Yes)
            msg_box.button(QMessageBox.Yes).setText('现在更新')
            if app_info["update_type"] != 0:
                msg_box.addButton(QMessageBox.No)
                msg_box.button(QMessageBox.No).setText('以后再说')
            msg_box.setDefaultButton(QMessageBox.Yes)
            reply = msg_box.exec()
            if reply == QMessageBox.Yes:
                self.win.setWindowTitle("正在下载新版,请稍后...")
                self.download(app_os_info["url"])
                return True
        return False

    def download(self, url: str):
        if "lanzou" in url:
            url = self.get_lanzou(url)

        res = requests.get(url, stream=True)
        content_size = int(res.headers["content-length"])
        chunk_size = 1024
        size = 0
        if res.status_code == 200:
            file_name = re.findall("filename=(.+)", res.headers["Content-Disposition"].replace(" ", ""))[0]
            with open(os.path.join(root_path, file_name), "wb") as f:
                for data in res.iter_content(chunk_size=chunk_size):
                    f.write(data)
                    size += len(data)  # 已下载文件大小
                    self.win.setWindowTitle("正在下载新版 - %s" % str(int(size / content_size * 100)))

    def get_lanzou(self, url):
        lanzou_id = re.findall("com/(.+)", url)[0]
        session = requests.session()
        headers = {
            "sec-ch-ua": '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            "Referer": "https://wequ.lanzoub.com/tp/" + lanzou_id,
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        iframe_res = session.get("https://wequ.lanzoub.com/tp/" + lanzou_id, headers=headers)
        url = re.findall("tedomain = '(.*?)'", iframe_res.text)
        file = re.findall("domianload = '(.*?)'", iframe_res.text)
        down_url = url[0] + file[0]
        down_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Cookie": "down_ip=1",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
        }
        res = session.head(down_url, headers=down_headers, allow_redirects=False)
        return res.headers["Location"]
