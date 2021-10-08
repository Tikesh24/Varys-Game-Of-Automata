from pynput.keyboard import Key,Listener
from pynput.mouse import Listener as mouseListn
# mouse_event = []
# Mouse and Kekboard listner for getting coordinates for the mouse and keyboard keys.

def start_listner():
    global keyboardListner, mouseListner
    keyboardListner=Listener
    mouseListner=mouseListn

    mouse_event = []
    def on_move(x, y):
        # print({"device": "mouse", "event": "move", "x": x, "y": y})
        mouse_event.append({"device": "mouse", "event": "move", "x": x, "y": y})

    def on_click(x, y, button, pressed):
        if pressed:
            print({"device": "mouse", "event": "click", "x": x, "y": y, "button": "{0}".format(button)})
            mouse_event.append({"device": "mouse", "event": "click", "x": x, "y": y, "button": "{0}".format(button)})

    def on_scroll(x, y, dx, dy):
        # print({"device": "mouse", "event": "scroll", "x": x, "y": y, "dx": dx, "dy": dy})
        mouse_event.append({"device": "mouse", "event": "scroll", "x": x, "y": y, "dx": dx, "dy": dy})

    def on_press(key):
        # print({"device": "keyboard", "event": "key-press", "key":key})
        mouse_event.append({"device": "keyboard", "event": "key-press", "key": str(key)})

    def on_release(key):
        if key == Key.esc:
            # Stop listeners
            listener.stop()
            return False

    with mouseListner(on_click=on_click) as listener:
        with keyboardListner(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    return mouse_event

# Listner for getting coordinates for taking screenshot area
def get_validation_image_coordinates():
    ss_coordinate = []

    def on_click(x, y, button, pressed):
        if pressed:
            # print({"device": "mouse", "event": "click_pressed", "x": x, "y": y, "button": "{0}".format(button)})
            ss_coordinate.append(x)
            ss_coordinate.append(y)
        else:
            # print({"device": "mouse", "event": "click_release", "x": x, "y": y, "button": "{0}".format(button)})
            ss_coordinate.append(x)
            ss_coordinate.append(y)

            listener.stop()
            return False

    def on_release(key):
        if key == Key.esc:
            # Stop listeners
            listener.stop()
            return False

    with mouseListner(on_click=on_click) as listener:
        with keyboardListner(on_release=on_release) as listener:
            listener.join()

    return ss_coordinate
