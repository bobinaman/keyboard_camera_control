from pynput import keyboard
import camera

#visit:
#https://pynput.readthedocs.io/en/latest/keyboard.html

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))

        process_key(key)

    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def process_key(key):

    if(key.char == "a"):
        camera.take_picture()
    if(key.char == "b"):
        camera.take_eyes_picture()


def on_activate():
    print('Global hotkey activated!')

def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<alt>+h'),
    on_activate)
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

