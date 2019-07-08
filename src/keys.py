import keyboard, mouse, time

def move(key, times=1):
    keyboard.press(key)
    time.sleep(.245 * times)
    keyboard.release(key)
def place(num):
    keyboard.press_and_release(num)
    keyboard.press("space")
    mouse.press("right")
    time.sleep(0.4)
    keyboard.release("space")
    mouse.release("right")
