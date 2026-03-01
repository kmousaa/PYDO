
import datetime
import colorama 
from colorama import Fore, Back, Style

# Welcome message 
print(Back.BLACK + Fore.WHITE + "=" * 60)
print(Back.BLACK + Fore.WHITE + "      ██████╗ ██╗   ██╗██████╗  ██████╗ ")
print(Back.BLACK + Fore.WHITE +"      ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔═══██╗")
print(Back.BLACK + Fore.WHITE +"      ██████╔╝ ╚████╔╝ ██║  ██║██║   ██║")
print(Back.BLACK + Fore.WHITE +"      ██╔═══╝   ╚██╔╝  ██║  ██║██║   ██║")
print(Back.BLACK + Fore.WHITE +"      ██║        ██║   ██████╔╝╚██████╔╝")
print(Back.BLACK + Fore.WHITE +"      ╚═╝        ╚═╝   ╚═════╝  ╚═════╝ ")
print("=" * 60)
print("   Welcome to PyDo, by Karim Mousa")
print("   The simplest Python terminal to-do list")
print("   Get started by typing \"help\" ")
print("=" * 60)


# Records all to-do list instances 
global_lists = {}
command = ""

# Helper function for date time
def ordinal(n):
    if 11 <= n % 100 <= 13:
        return str(n) + "th"
    elif n % 10 == 1:
        return str(n) + "st"
    elif n % 10 == 2:
        return str(n) + "nd"
    elif n % 10 == 3:
        return str(n) + "rd"
    else:
        return str(n) + "th"

# Class used to define to-do list
class todo: 
    def __init__(self,name):
        self.list_name = name
        self.date = datetime.datetime.now()
        self.todo_list = {}

    def print_list(self):
        # showcase list
        print()
        print(Fore.CYAN + "=" * 60)
        print("Name:              " + self.list_name)
        day = ordinal(self.date.day)
        month = self.date.strftime("%B")
        year = str(self.date.year)
        print("Creation Date:     " + self.date.strftime("%A ") + " " + day + " " + month + " " + year)
        print(Fore.CYAN + "=" * 60)
        print("LIST: ")
        print()
        for key, value in self.todo_list.items():
            mark = (Fore.GREEN + "✓") if value[1] else (Fore.RED + "✗")
            print(Fore.WHITE + f" ◉ {key:<3} ➱ {value[0]:<25} " + mark + Fore.WHITE)
        print(Fore.CYAN + "=" * 60)
        print()

        

# List Creation Functions in the main page 

def create_list(list_name):
    print()    
    if list_name not in global_lists:
        global_lists[parsed[1]] = todo(list_name)
        print(Fore.MAGENTA + "List \"" + list_name + "\" created successfully!" + Fore.RESET)
        select_list(list_name)
    else:
        print(Fore.RED + "ERROR: TODO List \"" + list_name + "\" already exists " + Fore.RESET)
    
def view_lists():
    print()
    print(Fore.MAGENTA + "=" * 60)
    if len(global_lists.keys()) == 0:
        print()
        print(Fore.MAGENTA + "        You have no TODO lists!")
    else:   
        print(Fore.MAGENTA + "          The user has the following lists:")
    print(Fore.MAGENTA + "=" * 60)
    for x in global_lists.values():
        x.print_list()
        print(Fore.MAGENTA + "=" * 60)
        print(Fore.MAGENTA + "=" * 60)

    print()
    print(Fore.MAGENTA + "=" * 60)

def select_list(list_name):
    print()
    if list_name not in global_lists:
        print(Fore.RED + "ERROR: List \"" + list_name + "\" does not exist " + Fore.RESET)
        ans = input(Fore.YELLOW + f'Create it now? (Y/N): ' + Fore.RESET)
        if ans == "y" or  ans == "Y":
            create_list(list_name)
        
    else:
        #global selector present 
        internal_command = ""
        print(Fore.MAGENTA + "List \"" + list_name + "\" has been selected!" + Fore.RESET)
        global_lists[list_name].print_list()

        # Run commands 
        print(Fore.CYAN + "Available commands: " + Fore.YELLOW + "add [task], del [task], com [task no] ,view, back" + Fore.RESET)
        list_instance = global_lists[list_name]
        while True:
            action = input(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.YELLOW  + ">> ")
            parsed = action.split(" ")
            if parsed[0] == "add":
                    list_instance.todo_list[str(len(list_instance.todo_list)+1)] = (''.join(parsed[1:]), False)
                    print(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.MAGENTA + "Task \"" + ' '.join(parsed[1:]) + "\" has been added to the list!" + Fore.RESET)


            # WORK IN PROGRESS
            elif parsed[0] == "com":
                    print(list_instance.todo_list)


            elif parsed[0] == "view":
                print(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.MAGENTA + "Here is your list:" + Fore.RESET)
                list_instance.print_list()
            
            elif parsed[0] == "back":
                print(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.MAGENTA + "Returning to main menu..." + Fore.RESET)
                break


            else:
                print(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.RED  + "ERROR: Command \"" + action + "\" is invalid")




                    

def list_help():
    print()
    print(Fore.CYAN + "=" * 60)
    print("Available commands:")
    print(Fore.CYAN + "➪ Create [list name] - Create a new to-do list with the specified name")
    print(Fore.CYAN + "➪ Select [list name] - To view a specific list")
    print(Fore.CYAN + "➪ View - View all lists")
    print(Fore.CYAN + "➪ Exit - Exit the program")
    print()
    print(Fore.CYAN + "=" * 60)




# Main selector 
while True:
    print()
    
    # Ask for the next action needed
    command = input(Fore.GREEN + "What action would you like to perform?" + Fore.YELLOW + "\n >> ")
    parsed = command.split(" ")

    if len(command) == 0:
        print()
        print(Fore.RED + "ERROR: Command cannot be empty" + Fore.RESET)
        continue

    elif len(parsed) == 1:
        print()
        print(Fore.RED + "ERROR: Command \"" + command + "\" is incomplete" + Fore.RESET)

    elif parsed[0] == "create":
        if parsed[1].strip() == "":
            print()
            print(Fore.RED + "ERROR: List name cannot be empty" + Fore.RESET)
        else:
            create_list(parsed[1].strip())
        
    elif parsed[0] == "view":
        view_lists()

    elif parsed[0] == "select":
        select_list(parsed[1])

    elif parsed[0] == "help":
        list_help()


    # End program
    elif parsed[0] == "exit":
        print()
        print(Fore.MAGENTA + "Exiting PyDo..." + Fore.RESET)
        break


    else:
        print()
        print(Fore.RED  + "ERROR: Command \"" + command + "\" is invalid")

# Exit Screen
print(Back.BLACK + Fore.GREEN + "=" * 60)
print(Fore.GREEN + "        Thanks for using PyDo!")
print(Fore.GREEN + "        Your tasks are safe 🐍")
print("=" * 60)

snake = r"""
            /^\/^\
        _|__|  O|
\/     /~     \_/ \
\____|__________/  \
        \_______      \
                `\     \                 \
                    |     |                  \
                /      /                    \
                /     /                       \\
                /      /                         \ \
            /     /                            \  \
            /     /             _----_            \   \
            /     /           _-~      ~-_         |   |
        (      (        _-~    _--_    ~-_     _/   |
            \      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
                ~--______-~                ~-___-~
"""

print(Fore.GREEN + snake)
print(Fore.GREEN + "=" * 60)
print(Fore.GREEN + "        Goodbye 👋")
print(Fore.GREEN + "        Stay productive.")
print(Fore.GREEN + "=" * 60)
print(Style.RESET_ALL)



      
 



