import configparser
from os import path

from utils.get_root_path import home_path

ini_path = path.join(home_path, "config.ini")

if path.exists(ini_path) is not True:
    with open(ini_path, "w") as f:
        f.write("""
[device]
id = 0
password = 0
auto_online = no
        """)

config = configparser.ConfigParser()
config.read(ini_path, encoding="utf8")


def get(section, option):
    return config.get(section, option)


def set(section, option, value):
    config.set(section, option, value)
    config.write(open(ini_path, 'w'))
