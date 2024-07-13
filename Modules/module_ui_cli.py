from typing import Union
from copy import deepcopy

class ModuleUICLI:
    def __init__(
            self
        ):

        self.__struct_menu_option: dict[str, Union[str, callable, None, bool]] = {
            "text": "",
            "task": None,
            "is_callable": False,
        }
        self.menu: list = []

    def set_Menu(self, menus: dict[str, Union[str, callable, None, bool, dict]]):
        self.menu = menus

    def get_Menu(self):
        return self.menu
    
    def add_menu_option(self, text: str, task: Union[callable, None]) -> dict:
        option = deepcopy(self.__struct_menu_option)
        option["text"] = text
        option["task"] = task
        option["is_callable"] = callable(task)

        self.menu.append(option)

    def print_menu(self, indent=0):
        indent_str = ' ' * indent
        for option in self.menu:
            print(f"{indent_str}Text: {option['text']}")
            print(f"{indent_str}Is Callable: {option['is_callable']}")
            

      
       



    def get_user_selection(self, text: str):
        selection = input(text)
        return self.menu.items.get(selection, None)
    
    
    def search_into_menu(self, selection, menu):
        for key, value in menu.items():
            if key == selection:
                return key, value
        return selection, None
                


    def serve_menu(self):
        self.print_menu()
        while True:
            user_selection = self.get_user_selection("Selection: ")
            if callable(user_selection["return"]):
                user_selection["return"]()
            elif isinstance(user_selection, dict):
                sub_menu = ModuleUICLI(user_selection)
                sub_menu.serve_menu()
            else:
                print("Invalid Selection!")
                break





