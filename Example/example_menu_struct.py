from pprint import pprint
from copy import deepcopy

def __menu_volume_set():
    print("__menu_volume_set")


from typing import Union  

"""
struct_menu_option: list[str, Union[callable, list, None], bool] = ["", None, False]
menu = struct_menu_option.copy()
menu[0] = "m-Level0"
menu[1] = []

example_menu_option_1 = struct_menu_option.copy()
example_menu_option_1[0] = "m-Level1"
example_menu_option_1[1] = __menu_volume_set

example_menu_option_2 = struct_menu_option.copy()
example_menu_option_2[0] = "m-Level2"
example_menu_option_2[1] = struct_menu_option.copy()
example_menu_option_2[1][0] = "m-Level3"
example_menu_option_2[1][1] = lambda: print("called beta function!")

menu[1].append(example_menu_option_1)
menu[1].append(example_menu_option_2)
"""

struct_menu_option: dict[str, Union[str, callable, None, bool, dict]] = {
    "text": "",
    "return": None,
    "is_callable": False,
    "sub_menu": []
}
# MENU 0
menu = deepcopy(struct_menu_option)
menu["text"] = "MENU"

# MENU 1 - MENU->SETTINGS
menu["sub_menu"].append(deepcopy(struct_menu_option))
menu["sub_menu"][-1]["text"] = "Settings"
menu["sub_menu"][-1]["sub_menu"].append(deepcopy(struct_menu_option))

# MENU 2 - MENU->SETTINGS->SET VOLUME
menu["sub_menu"][-1]["sub_menu"][-1]["text"] = "Set Volume"
menu["sub_menu"][-1]["sub_menu"][-1]["return"] = lambda: print("called a function!")
menu["sub_menu"][-1]["sub_menu"][-1]["is_callable"] = True

# MENU 2 - MENU->SETTINGS->GET VOLUME
menu["sub_menu"][-1]["sub_menu"].append(deepcopy(struct_menu_option))
menu["sub_menu"][-1]["sub_menu"][-1]["text"] = "Get Volume"
menu["sub_menu"][-1]["sub_menu"][-1]["return"] = lambda: print("called a function!")
menu["sub_menu"][-1]["sub_menu"][-1]["is_callable"] = True

pprint(menu)