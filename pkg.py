import os
import subprocess
import sys

print("正在准备")
root_path = os.getcwd()


def local_rm(dirpath):
    if os.path.exists(dirpath):
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


if os.path.exists(os.path.join(root_path, "build")):
    print("清空build目录")
    local_rm(os.path.join(root_path, "build"))

if os.path.exists(os.path.join(root_path, "dist")):
    print("清空dist目录")
    local_rm(os.path.join(root_path, "dist"))

del_mod_list = []
pyinstaller_path = ""
pkg_shell = ""
print(sys.platform)
if sys.platform == 'win32':
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

print(pyinstaller_path)
print("正在打包...")
subprocess.Popen("{} --clean {} -n WeDuck".format(pyinstaller_path, pkg_shell), stderr=subprocess.PIPE,
                 stdout=subprocess.PIPE, shell=True).stdout.readline()
print("{} --clean {} -n WeDuck".format(pyinstaller_path, pkg_shell))
print("生成打包文件完成")
del_path = os.path.join(root_path, "dist", "WeDuck", "PySide2")
for d in del_mod_list:
    print("清理打包文件无用的依赖 %s" % d)
    os.remove(os.path.join(del_path, d))

print("清理打包文件无用的翻译文件")
local_rm(os.path.join(del_path, "translations"))
print("打包完成，目录：" + os.path.join(os.getcwd(), "dist", "WeDuck"))
