import os
import subprocess
import sys

print("正在打包...")
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
        os.rmdir(dirpath)


if os.path.exists(os.path.join(root_path, "build")):
    print("清空build目录")
    local_rm(os.path.join(root_path, "build"))

if os.path.exists(os.path.join(root_path, "dist")):
    print("清空dist目录")
    local_rm(os.path.join(root_path, "dist"))

spec = ""
del_mod_list = []

if sys.platform == 'win32':
    spec = "pkg_win.spec"
    del_mod_list = ["d3dcompiler_47.dll", "Qt5Pdf.dll", "Qt5Quick.dll", "opengl32sw.dll",
                    "libEGL.dll", "Qt5Svg.dll", "libGLESv2.dll", "Qt5DBus.dll", "Qt5WebSockets.dll"]
elif sys.platform == 'linux':
    spec = "pkg_linux.spec"
else:
    spec = "pkg_mac.spec"

print("使用%s打包" % spec)
pkg_spec_ptah = os.path.join(root_path, "spec", spec)
pyinstaller_path = os.path.join(root_path, "venv", "Scripts", "pyinstaller")

subprocess.Popen("{} --clean {}".format(pyinstaller_path, pkg_spec_ptah), stderr=subprocess.PIPE,
                 stdout=subprocess.PIPE, shell=True).stdout.readline()
print("生成打包文件完成")
del_path = os.path.join(root_path, "dist", "WeDuck", "PySide2")
for d in del_mod_list:
    print("清理打包文件无用的依赖 %s" % d)
    os.remove(os.path.join(del_path, d))

print("清理打包文件无用的翻译文件")
local_rm(os.path.join(del_path, "translations"))
print("打包完成，目录：" + os.path.join(os.getcwd(), "dist", "WeDuck"))
