import pyautogui
import PIL
import re
from pynput.mouse import Listener
import pyperclip


class Color():
    def __init__(self):
        raw_coords = str(pyautogui.position())

        raw_coords = raw_coords.split(",")

        coords = []

        for item in raw_coords:
            single = int(re.sub("[^0-9]", "", item))
            coords.append(single)

        sceenshot = pyautogui.screenshot()
        sceenshot.save(r'screen.png')

        image = PIL.Image.open("screen.png")

        x = coords[0]
        y = coords[1]


        pixel_value_rgb = image.getpixel((x,y))
        pixel_value_hex = '#%02x%02x%02x' % pixel_value_rgb

        self.rgb = pixel_value_rgb
        self.hex = pixel_value_hex


def on_click(x, y, button, pressed):
    if not pressed:
        hex = str(Color().hex)
        pyperclip.copy(hex)
        return False

with Listener(
        on_click=on_click) as listener:
    listener.join()

