import configparser
from os import path
from g import VERSION
from utils.get_root_path import root_path
ini_path = path.join(root_path, "config.ini")
if path.exists(ini_path) is not True:
    with open(ini_path, "w") as f:
        f.write("""
[app]
debug = off
version = %s

[device]
id = 0
password = 0
auto_online = no
        """ % VERSION)

config = configparser.ConfigParser()
config.read(ini_path, encoding="utf8")


def get(section, option):
    return config.get(section, option)


def set(section, option, value):
    config.set(section, option, value)
    config.write(open(ini_path, 'w'))
