from Modules.module_ui_cli import ModuleUICLI
from Modules.module_settings import ModuleSettings
from copy import deepcopy


 
module_settings_instance = ModuleSettings()

def __menu_volume_set():
    volume = int(input("Volume Level (0-100): "))
    try:
        module_settings_instance.set_volume(volume)
        
    except Exception as error:
        print("> ERROR: ", error)

from typing import Union

struct_menu_option: dict[str, Union[str, callable, None, bool, dict]] = {
    "text": "",
    "return": None,
    "is_callable": False,
    "sub_menu": []
}
cli = ModuleUICLI()
cli.add_menu_option("deneme",print("deneme1"))
cli.print_menu()







