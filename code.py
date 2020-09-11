from keyboard import *
from keymaps import *

keyboard = Keyboard()

keyboard.keymap = MAC_MAP
keyboard.profiles = {
    "BT1": IOS_MAP,
    "BT3": WIN_MAP
}

# HACK: Store it here
keyboard.brigntness = 0

def increase_backlight(dev, n, is_down):
    if is_down:
        print("Increasing brightness")
        if keyboard.brigntness==0:
            keyboard.backlight.on()
        keyboard.brigntness += 25
        if keyboard.brigntness > 250:
            keyboard.brigntness = 250
        keyboard.backlight.set_brightness(keyboard.brigntness)
        keyboard.backlight.update()

def decrease_backlight(dev, n, is_down):
    if is_down:
        print("Decreasing brightness")
        keyboard.brigntness -= 25
        if keyboard.brigntness<0:
            keyboard.brigntness = 0
        if keyboard.brigntness == 0:
            keyboard.backlight.off()
        else:
            keyboard.backlight.set_brightness(keyboard.brigntness)
            keyboard.backlight.update()

macro_table = {
    8: increase_backlight,
    9: decrease_backlight,
}

def macro_handler(dev, n, is_down):
    if n in macro_table:
        macro_table[n](dev, n, is_down)
        return

    if is_down:
        print("Macro %d is pressed but no handler defined." % n)
    else:
        print("Macro %d is release but no handler defined." % n)

def pairs_handler(dev, n):
    dev.send_text('You just triggered pair keys #{}\n'.format(n))


keyboard.macro_handler = macro_handler
keyboard.pairs_handler = pairs_handler

# ESC   1   2   3   4   5   6   7   8   9   0   -   =  BACKSPACE
# TAB   Q   W   E   R   T   Y   U   I   O   P   [   ]   |
# CAPS  A   S   D   F   G   H   J   K   L   ;   "      ENTER
#LSHIFT Z   X   C   V   B   N   M   ,   .   /         RSHIFT
# LCTRL LGUI LALT          SPACE         RALT MENU  L1 RCTRL
#
#   0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13,
#   27,26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14,
#   28,29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,     40,
#   52,51, 50, 49, 48, 47, 46, 45, 44, 43, 42,         41,
#   53,  54, 55,             56,           57, 58, 59, 60

# Pairs: J & K, U & I
#keyboard.pairs = [{35, 36}, {20, 19}]

keyboard.run()
