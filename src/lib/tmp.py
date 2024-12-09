from global_hotkeys import *

import time

# Flag to indicate whether the program should continue running.
is_alive = True

def print_hello():
    print("Hello")

def print_world():
    print("World")

def print_foo():
    print("Foo")

def print_bar():
    print("Bar")

def print_with_params(params):
    print(params["test"])

def press_with_params(params):
    print(params["press_param"])

def release_with_params(params):
    print(params["release_param"])

def exit_application():
    global is_alive
    print("exiting")
    stop_checking_hotkeys()
    is_alive = False


# Declare some key bindings.
bindings = [
    ["control + 7, control + 4", None, print_world, True],
    # You can use direct keycodes as well (useful for non-US keyboard layouts):
    # ["control + 0x35", None, print_hello, False], # 0x35 is the keycode for the '5' key
    # ["control + 6", None, print_with_params, False, {"test":5}],
    # [
    #     "control + 8", 
    #     press_with_params, 
    #     release_with_params, 
    #     False, 
    #     {"press_param":"pressed!"}, 
    #     {"release_param": "released!"}
    # ],
    # # dict style
    # {
    #     "hotkey": "control + 4",
    #     "on_press_callback": None,
    #     "on_release_callback": print_with_params,
    #     "actuate_on_partial_release": False,
    #     "callback_params": {"test": "testing"},

    # },
    # # dict style with differentiating params for press and release callbacks
    # {
    #     "hotkey": "control + 9",
    #     "on_press_callback": press_with_params,
    #     "on_release_callback": release_with_params,
    #     "actuate_on_partial_release": False,
    #     "press_callback_params": {"press_param":"ctrl+9 pressed!"},
    #     "release_callback_params": {"release_param": "ctrl+9 released!"},

    # },

    # ["window + 1", None, print_foo, False],
    # ["t,m", None, print_bar, False],
    # ["control + Q", None, exit_application, False],
]

# Bindings take on the form of:
#   <binding>, on_press_callback, on_release_callback, actuate_on_partial_release_flag, callback_params
#
# *Note that callback_params will be passed to both press and release callback functions
#
# Or in explicit dict format:
# {
#     "hotkey": <binding>,
#     "on_press_callback": <press_callback>,
#     "on_release_callback": <release_callback>,
#     "actuate_on_partial_release": False | True,
#     "callback_params": <a variable or expression can go here>  <-- This applies to both callbacks.
#     "press_callback_params": <a variable or expression can go here>
#     "release_callback_params": <a variable or expression can go here>
# }

# It's useful to have 'actuate_on_partial_release_flag' set to False, 
# so your modifier keys don't get in the way of any automatic keyboard output you're doing in response.

# Note the actual hotkey syntax. Key combinations are denoted via the '+' character, 
# and additional key chords are separated by commas. Spaces are ignored.

# Register all of our keybindings
register_hotkeys(bindings)

# Finally, start listening for keypresses
start_checking_hotkeys()

# Keep waiting until the user presses the exit_application keybinding.
# Note that the hotkey listener will exit when the main thread does.
while is_alive:
    time.sleep(0.1)