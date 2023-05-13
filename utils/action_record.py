import json
import os
import time

from pynput import mouse, keyboard

from utils.get_root_path import home_path

script_path = os.path.join(home_path, "script")


class ActionRecord:
    def __init__(self, name):
        self.name = name
        self.thread_mouse = None
        self.thread_keyboard = None
        self.record = []

    def run(self):
        with mouse.Listener(on_click=self.on_mouse_click, on_scroll=self.on_scroll) as self.thread_mouse, \
                keyboard.Listener(on_press=self.on_keyboard_press,
                                  on_release=self.on_keyboard_release) as self.thread_keyboard:
            self.thread_mouse.join()
            self.thread_keyboard.join()

    def on_mouse_click(self, x, y, click, pressed):
        self.record.append({'x': x, "y": y, "button": str(click), "action": "pressed" if pressed else 'released',
                            "_time": time.time()})

    def on_keyboard_press(self, key):
        """
        按键时记录所按下的键
        :param key:
        :return:
        """
        if key != keyboard.Key.esc:
            try:
                self.record.append({"key": key.char, "action": "pressed_key", "_time": time.time()})
            except AttributeError:
                self.record.append({"key": str(key), "action": "pressed_key", "_time": time.time()})

    def on_keyboard_release(self, key):
        """
        释放按键处理函数
        :param key:
        :return:
        """
        if key == keyboard.Key.esc:
            self.thread_mouse.stop()
            self.thread_keyboard.stop()
            if not os.path.exists(script_path):
                os.makedirs(script_path)
            with open(os.path.join(script_path, self.name), mode="w", encoding="utf-8") as s:
                s.write(json.dumps(self.record))
        else:
            try:
                self.record.append({"key": key.char, "action": "released_key", "_time": time.time()})
            except AttributeError:
                self.record.append({"key": str(key), "action": "released_key", "_time": time.time()})

    def on_scroll(self, x, y, dx, dy):
        json_object = {'action': 'scroll', 'vertical_direction': int(dy), 'horizontal_direction': int(dx), 'x': x,
                       'y': y, '_time': time.time()}
        self.record.append(json_object)
