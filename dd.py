from typing import Union, Callable

class ModuleUICLI:
    def __init__(
            self, 
            menu: dict[str, Union[Callable, dict[str, Union[Callable, dict]]]]
        ):
        self.menu = menu

    def set_Menu(self, menus: dict[str, Union[Callable, dict[str, Union[Callable, dict]]]]):
        self.menu = menus

    def get_Menu(self):
        return self.menu

    def print_menu(self, menu=None):
        
        if menu is None:
            menu = self.menu
            print("=== MENU ===\n")
        for key, value in menu.items():
            print(f" > {key}", end="")
            if callable(value):
                print(f" -> {value.__name__}")
            else:
                self.print_menu(value)

    def get_user_selection(self, text: str):
        selection = input(text)

        for key, value in self.menu.items():

            if key == selection:
                return key, value
            elif not callable(value) and type(value) is dict:
                sub_key, sub_value = self.search_into_menu(
                    selection = selection,
                    menu = value
                )
                if callable(sub_value):
                    return sub_key, sub_value
                else:
                    pass
            else:
                continue

        return selection, None
    
    def search_into_menu(self, selection, menu):
        for key, value in menu.items():
            if key == selection:
                return key, value
        return selection, None
                


    def serve_menu(self):
        self.print_menu()
        user_selection, menu_value = self.get_user_selection("Selection: ")
        return user_selection, menu_value


if __name__ == "__main__":
    def find_and_execute(menu, selection):
        if selection in menu:
            if callable(menu[selection]):
                parameter = input(" a parameter value if exist: ")
                if parameter != "":
                    menu[selection](parameter)
                else:
                    menu[selection]()
            elif isinstance(menu[selection], dict):
                print(f"{selection} is a submenu.")
            else:
                print("Invalid selection.")
        else:
            found = False
            for key,value in menu.items():
                if isinstance(value, dict):
                    find_and_execute(value, selection)
                    found = True
            if not found:
                print("Wrong Selection.")


    from module_settings import ModuleSettings
    module_settings_instance = ModuleSettings()

    def function_example_1(param):
        try:
            new_volume = module_settings_instance.set_volume(int(param))
            print(f"Volume set to: {new_volume}")
        except Exception as e:
            print(e)

    def function_example_2(param):
        try:
            new_volume = module_settings_instance.set_volume(int(param))
            print(f"Volume set to: {new_volume}")
            current_volume = module_settings_instance.get_volume()
            print(f"Current Volume: {current_volume}")
        except Exception as e:
            print(e)

    def function_example_3():
        print("ex3")

    def exit():
        print("")

    menus = {
        "Files": {
            "ntf":module_settings_instance.get_volume,
            "nf": module_settings_instance.set_volume,
            "nw": function_example_3,
            "open recent": {
                "salsa.py": function_example_2,
                "beta.py": function_example_2,
                "deep": {
                    "deeper.py": function_example_1,
                    "deeper2.py": function_example_2,
                    "wer": {
                        "in" : function_example_2,
                        "for": function_example_3,
                    }
                },
            },
            "e": exit,
        }
    }

    module_ui_cli_instance = ModuleUICLI(menu=menus)
    module_ui_cli_instance.print_menu()
    
    while True:
        selection = module_ui_cli_instance.get_user_selection("> Selection: ")
        if selection == "e":
            print("Exiting menu.")
            break

        find_and_execute(menus, selection)  

        """def get_user_selection(self, text: str):
        selection = input(text)

        for item in self.menu["sub_menu"]:
            if item['text'].lower() == selection.lower():
                if item['is_callable']:
                    return item['return']
                elif item['sub_menu']:
                    return item
        return None"""

        """def get_user_selection(self, text: str):
        selection = input(text)

        for item in self.menu["sub_menu"]:
            if item['text'].lower() == selection.lower():
                if item['is_callable']:
                    return item['return']
                elif item['sub_menu']:
                    return item
        return None

    def serve_menu(self):
        self.print_menu()
        user_selection = self.get_user_selection("Selection: ")
        if callable(user_selection):
            user_selection()
        elif isinstance(user_selection, dict):
            sub_menu = ModuleUICLI(user_selection)
            sub_menu.serve_menu()
"""