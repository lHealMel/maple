from pynput import keyboard
import time


def press(key):
    print('Key %s pressed' % key)


def release(key):
    print(key)
    a = key
    str(a)
    int(a)
    print(type(a))



with keyboard.Listener(on_press=press, on_release=release) as listener: listener.join()
