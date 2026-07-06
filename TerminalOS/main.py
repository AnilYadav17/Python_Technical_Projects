from boot import boot_loading
from desktop import desktop_loading
from applications import display_apps
from applications import utilities
from applications import mini_terminal
from applications import settings
from applications import help
from applications import calculator
from applications import about
from core.ui import clear_screen, pause, show_message

clear_screen()
boot_loading.load()
boot_loading.security()


if boot_loading.LOGGED_IN == True:
    desktop_loading.load()
    while True:
        try:
            choice = int(input("Choice > "))
        except ValueError:
            break


        match choice:
            case 1:
                display_apps.display_main()
            case 2:
                show_message("\nFeature under construction!", style="yellow")
                pause()
                clear_screen()
                desktop_loading.load()
            case 3:
                utilities.display_utils()
                clear_screen()
                desktop_loading.load()
            case 4:
                mini_terminal.terminal_main()
                clear_screen()
                desktop_loading.load()
            case 5:
                settings.settings_main()
                clear_screen()
                desktop_loading.load()
            case 6:
                help.help_main()
                clear_screen()
                desktop_loading.load()
            case 7:
                calculator.calc_main()
                clear_screen()
                desktop_loading.load()
            case 8:
                about.about_main()
                clear_screen()
                desktop_loading.load()
            case 9:
                clear_screen()
                show_message("Logging out...", style="cyan")
                break
            case 0:
                clear_screen()
                show_message("Shutting down...", style="cyan")
                break
            case _:
                show_message("\nFeature under construction!", style="yellow")
                pause()
                clear_screen()
                desktop_loading.load()
    
else:
    pass