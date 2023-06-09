# -*- coding: utf-8 -*-
import codecs
import datetime
import os
import subprocess
import sys

local = False  # False代表Github打包环境，True代表本地

print("Create Version")
root_path = os.getcwd()
time_now = str((datetime.datetime.utcnow() + datetime.timedelta(hours=8)))
VERSION = time_now.replace("-", "").replace(" ", "")[0:10]
print("version is " + VERSION)

print("Set Config Version")
with open(os.path.join(root_path, "g.py"), "w", encoding="utf8") as f:
    f.write(
        """STOP_MQ = False
VERSION = %s""" % VERSION)


def set_window_nsi():
    print("Set install nsi Version")
    with codecs.open(os.path.join(root_path, "install_tpl.nsi"), "r", encoding="utf8") as n1:
        nsi = n1.read()
        nsi = nsi.replace("WeDuckVersion", VERSION)

    with codecs.open(os.path.join(root_path, "install.nsi"), "w", encoding="gbk") as n2:
        n2.write(nsi)
    print("Set install nsi Version Ok")


def local_rm(dirpath):
    if os.path.exists(dirpath):
        try:
            files = os.listdir(dirpath)
            for file in files:
                filepath = os.path.join(dirpath, file).replace("\\", '/')
                if os.path.isdir(filepath):
                    local_rm(filepath)
                else:
                    os.remove(filepath)
            try:
                os.rmdir(dirpath)
            except:
                pass
        except:
            os.remove(dirpath)


if os.path.exists(os.path.join(root_path, "build")):
    print("clean build")
    local_rm(os.path.join(root_path, "build"))

if os.path.exists(os.path.join(root_path, "dist")):
    print("clean dist")
    local_rm(os.path.join(root_path, "dist"))

del_mod_list = []
pyinstaller_path = ""
pkg_shell = ""
print(sys.platform)
if sys.platform == 'win32':
    set_window_nsi()
    pkg_shell = '-y -i="icon.ico" -D -w main.py --add-data="icon.png;." --add-data="icon.ico;."'
    pyinstaller_path = os.path.join(root_path, "venv", "Scripts", "pyinstaller")
    del_mod_list = ["d3dcompiler_47.dll", "Qt5Pdf.dll", "Qt5Quick.dll", "opengl32sw.dll",
                    "libEGL.dll", "Qt5Svg.dll", "libGLESv2.dll", "Qt5DBus.dll", "Qt5WebSockets.dll"]
elif sys.platform == 'linux':
    pkg_shell = '-y -i="icon.ico" -D -w main.py --add-data="icon.png:." --add-data="icon.ico:."'
else:
    pkg_shell = '-y -i="icon.icns" -D -w main.py --add-data="icon.icns:." --add-data="icon.ico:."'
    pyinstaller_path = os.path.join(root_path, "venv", "bin", "pyinstaller")
    del_mod_list = []

if local is not True:
    pyinstaller_path = "pyinstaller"

print("pkg...")
subprocess.Popen("{} --clean {} -n WeDuck".format(pyinstaller_path, pkg_shell), stderr=subprocess.PIPE,
                 stdout=subprocess.PIPE, shell=True).stdout.readline()
print("{} --clean {} -n WeDuck".format(pyinstaller_path, pkg_shell))
print("pkg done!")
del_path = os.path.join(root_path, "dist", "WeDuck", "PySide2")
for d in del_mod_list:
    print("delete module %s" % d)
    os.remove(os.path.join(del_path, d))

print("delete translate")
local_rm(os.path.join(del_path, "translations"))

if local is True:
    print("delete nsi")
    local_rm(os.path.join(root_path, "install.nsi"))
    print("delete spec")
    local_rm(os.path.join(root_path, "WeDuck.spec"))

    if sys.platform == "darwin":
        os.system('''
        create-dmg --volname "WeDuck" --window-pos 200 220 --window-size 500 300 --icon-size 100 --icon "WeDuck.app" 100 100 --hide-extension "WeDuck.app" --app-drop-link 300 100 "WeDuckInstall.dmg" "dist/WeDuck.app"
        ''')

print("done dir:" + os.path.join(os.getcwd(), "dist", "WeDuck"))