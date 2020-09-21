from keyboard import *

___ = TRANSPARENT
BOOT = BOOTLOADER
L1 = LAYER_TAP(1)
L2CAP = LAYER_TAP(2, CAPS)
L3MENU = LAYER_TAP(3, MENU)
LSFT4 = LAYER_MODS(4, MODS(LSHIFT))
RSFT4 = LAYER_MODS(4, MODS(RSHIFT))
LGUI5 = LAYER_MODS(5, MODS(LGUI))

def CTRL_(key):
    return MODS_KEY(MODS(CTRL), key)

def ALT_(key):
    return MODS_KEY(MODS(LALT), key)

FN_LAYER = (
    '`',  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
    ___, ___,  UP, ___, ___, ___, ___, ___, ___, ___,PGUP,UP,PGDN,___,
    ___,LEFT,DOWN,RIGHT,___, ___, ___, ___, ___, ___, LEFT, RIGHT,      ___,
    ___, ___, ___, ___, ___,BOOT, ___, ___, MACRO(8), MACRO(9), DOWN,       ___,
    ___, ___, ___,                ___,               ___, ___, ___,  ___
)

BT_LAYER = (
    BT_TOGGLE,BT1,BT2, BT3,BT4,BT5,BT6,BT7, BT8, BT9, BT0, ___, ___, ___,
    RGB_MOD, ___, ___, ___, ___, ___,___,USB_TOGGLE,___,___,___,___,___, ___,
    ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,      ___,
    ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,           ___,
    ___, ___, ___,                ___,               ___, ___, ___,  ___
)

TILDA_LAYER = (
    '`', ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,      ___,
    ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,           ___,
    ___, ___, ___,                ___,               ___, ___, ___,  ___
)

MAC_MAP = (
    # layer 0
    (
        ESC,   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, '-', '=', BACKSPACE,
        TAB,   Q,   W,   E,   R,   T,   Y,   U,   I,   O,   P, '[', ']', '|',
        L2CAP, A,   S,   D,   F,   G,   H,   J,   K,   L, ';', '"',    ENTER,
        LSFT4, Z,   X,   C,   V,   B,   N,   M, ',', '.', '/',         RSFT4,
        LCTRL, LALT,LGUI5,          SPACE,            RALT, L3MENU,  L1, RCTRL
    ),

    # layer 1
    FN_LAYER,

    # layer 2
    (
        '`',  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
        ___, ___, ___, CTRL_(E), ___, ___, ___,HOME,  UP,END, PGUP,AUDIO_VOL_DOWN,AUDIO_VOL_UP,AUDIO_MUTE,
        ___, CTRL_(A), ___, CTRL_(D), CTRL_(F), ___, ___,LEFT,DOWN,RIGHT, PGDN, ___,      ___,
        ___, ___, ___, CTRL_(C), ___, CTRL_(B), ___, ___, ___, ___, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),

    # layer 3
    BT_LAYER,

    # layer 4
    TILDA_LAYER,

    # layer 5
    (
        '`', ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,      ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),
)

IOS_MAP = (
    # layer 0
    (
        ESC,   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, '-', '=', BACKSPACE,
        TAB,   Q,   W,   E,   R,   T,   Y,   U,   I,   O,   P, '[', ']', '|',
        L2CAP, A,   S,   D,   F,   G,   H,   J,   K,   L, ';', '"',    ENTER,
        LSFT4, Z,   X,   C,   V,   B,   N,   M, ',', '.', '/',         RSFT4,
        LCTRL, LALT,LGUI5,          SPACE,            RALT, L3MENU,  L1, RCTRL
    ),

    # layer 1
    FN_LAYER,

    # layer 2
    (
        '`',  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
        ___, ___, ___, CTRL_(E), ___, ___, ___,HOME,  UP,END, PGUP,AUDIO_VOL_DOWN,AUDIO_VOL_UP,AUDIO_MUTE,
        ___, CTRL_(A), ___, CTRL_(D), CTRL_(F), ___, ___,LEFT,DOWN,RIGHT, PGDN, ___,      ___,
        ___, ___, ___, CTRL_(C), ___, CTRL_(B), ___, ___, ___, ___, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),

    # layer 3
    BT_LAYER,

    # layer 4
    TILDA_LAYER,

    # layer 5
    (
        '`', ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,      ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,           ___,
        ___, ___, ___,              CTRL_(SPACE),        ___, ___, ___,  ___
    ),
)

LGUI5X = LAYER_TAP(5, LGUI)
def WIN_(key):
    return MODS_KEY(MODS(LGUI), key)


WIN_MAP = (
    # layer 0
    (
        ESC,   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, '-', '=', BACKSPACE,
        TAB,   Q,   W,   E,   R,   T,   Y,   U,   I,   O,   P, '[', ']', '|',
        L2CAP, A,   S,   D,   F,   G,   H,   J,   K,   L, ';', '"',    ENTER,
        LSFT4, Z,   X,   C,   V,   B,   N,   M, ',', '.', '/',         RSFT4,
        LCTRL, LALT,LGUI5X,          SPACE,            RALT, L3MENU,  L1, RCTRL
    ),

    # layer 1
    FN_LAYER,

    # layer 2
    (
        '`',  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
        ___, ___, ___, CTRL_(E), ___, ___, ___,HOME,  UP,END, PGUP,AUDIO_VOL_DOWN,AUDIO_VOL_UP,AUDIO_MUTE,
        ___, CTRL_(A), ___, CTRL_(D), ___, ___, ___,LEFT,DOWN,RIGHT, PGDN, ___,      ___,
        ___, ___, ___, CTRL_(C), ___, ___, ___, ___, ___, ___, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),

    # layer 3
    BT_LAYER,

    # layer 4
    TILDA_LAYER,

    # layer 5
    (
        WIN_(ESC), WIN_(1), WIN_(2), WIN_(3), WIN_(4), WIN_(5), WIN_(6), WIN_(7), WIN_(8), WIN_(9), WIN_(0), WIN_('-'), WIN_('='), WIN_(BACKSPACE),
        ALT_(TAB), WIN_(Q), CTRL_(F4), WIN_(E), WIN_(R), CTRL_(T), WIN_(Y), WIN_(U), WIN_(I), WIN_(O), WIN_(P), WIN_('['), WIN_(']'), WIN_('|'),
        ___, CTRL_(A), CTRL_(S), CTRL_(D), CTRL_(F), WIN_(G), WIN_(H), WIN_(J), WIN_(K), CTRL_(L), WIN_(';'), WIN_('"'),      WIN_(ENTER),
        WIN_(LSHIFT), CTRL_(Z), CTRL_(X), CTRL_(C), CTRL_(V), WIN_(B), CTRL_(N), WIN_(M), WIN_(','), WIN_('.'), WIN_('/'),           WIN_(RSHIFT),
        WIN_(LCTRL), WIN_(LALT), LGUI,                WIN_(SPACE),               WIN_(MENU), WIN_(RALT), L1,  WIN_(RCTRL)
    ),
)
