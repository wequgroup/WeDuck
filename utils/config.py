import configparser
from os import getcwd, path

ini_path = path.join(getcwd(), "config.ini")
config = configparser.ConfigParser()
config.read(ini_path, encoding="utf8")


def get(section, option):
    return config.get(section, option)


def set(section, option, value):
    config.set(section, option, value)
    config.write(open(ini_path, 'w'))
