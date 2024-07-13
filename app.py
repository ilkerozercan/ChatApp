from Modules.module_ui_cli import Menu


if __name__ == "__main__":
    menu = Menu()
    menu.run()

from Modules.module_ui_cli import Menu


if __name__ == "__main__":
    menu = Menu()
    menu.run()

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