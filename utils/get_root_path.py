import os
import pathlib

root_path = os.path.dirname(__file__).replace("/utils", "").replace("\\utils", "")
home_path = os.path.join(str(pathlib.Path.home()), "WeDuck")
if os.path.exists(root_path) is not True:
    os.mkdir(root_path)
if os.path.exists(home_path) is not True:
    os.mkdir(home_path)
