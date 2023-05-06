import time

from pynput import mouse, keyboard


class ActionRecord:
    def __init__(self, name):
        self.name = name
        self.thread_mouse = mouse.Listener(on_click=self.on_mouse_click, on_scroll=self.on_scroll)
        self.thread_keyboard = keyboard.Listener(on_press=self.on_keyboard_press, on_release=self.on_keyboard_release)
        self.record = []

    def run(self):
        with self.thread_mouse as m, self.thread_keyboard as k:
            m.join()
            k.join()

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
            print(self.record)
        else:
            try:
                self.record.append({"key": key.char, "action": "released_key", "_time": time.time()})
            except AttributeError:
                self.record.append({"key": str(key), "action": "released_key", "_time": time.time()})

    def on_scroll(self, x, y, dx, dy):
        json_object = {'action': 'scroll', 'vertical_direction': int(dy), 'horizontal_direction': int(dx), 'x': x,
                       'y': y, '_time': time.time()}
        self.record.append(json_object)
