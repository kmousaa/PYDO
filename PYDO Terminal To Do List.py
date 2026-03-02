
import datetime
import colorama 
from colorama import Fore, Back, Style

# Welcome message 

colorama.init()
colorama.init()
print(Back.BLACK, end="")
print(Fore.WHITE + "=" * 60 + "   ")
print(Fore.WHITE + "      ██████╗ ██╗   ██╗██████╗  ██████╗                        ")
print(Fore.WHITE +"      ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔═══██╗                       ")
print(Fore.WHITE +"      ██████╔╝ ╚████╔╝ ██║  ██║██║   ██║                       ")
print(Fore.WHITE +"      ██╔═══╝   ╚██╔╝  ██║  ██║██║   ██║                       ")
print(Fore.WHITE +"      ██║        ██║   ██████╔╝╚██████╔╝                       ")
print(Fore.WHITE +"      ╚═╝        ╚═╝   ╚═════╝  ╚═════╝                        ")
print("=" * 60 + "   ") 
print("   Welcome to PyDo, by Karim Mousa                             ")
print("   The simplest Python terminal to-do list                     ")
print("   Get started by typing \"help\"                                ")
print("=" * 60)
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
    
    def complete(self,num):
        print(self.todo_list[num])
        self.todo_list[num][1] = True 

    def uncomplete(self,num):
        self.todo_list[num][1] = False 

    def delete(self,num):
        self.todo_list.pop(num)

    def print_list(self):
        # showcase list
        print()
        print(Fore.CYAN + "=" * 60)

        # Main metadata
        print(Fore.CYAN +  f"{'Name:':15} {Fore.LIGHTYELLOW_EX + self.list_name}")

        day = ordinal(self.date.day)
        month = self.date.strftime("%B")
        year = str(self.date.year)

        print(Fore.CYAN + f"{'Date:':15} {Fore.LIGHTMAGENTA_EX + self.date.strftime("%A ") + " " + day + " " + month + " " + year}")
        print()

        #Interesting Metadata
        print(Fore.LIGHTYELLOW_EX)
        print(Fore.CYAN + f"{'Total Tasks:':15} {Fore.LIGHTBLUE_EX + str(len(self.todo_list)) }")
        print(Fore.CYAN + f"{'Completed:':15} {Fore.GREEN + str(len([x for x in self.todo_list.values() if x[1] == True]))}")
        print(Fore.CYAN + f"{'Uncompleted:':15} {Fore.RED + str(len([x for x in self.todo_list.values() if x[1] == False]))}")
        print(Fore.CYAN + f"{'Completion:':15} {Fore.WHITE  + str(round(len([x for x in self.todo_list.values() if x[1] == True])/len(self.todo_list)*100, 2)) + Fore.WHITE + '%' if len(self.todo_list) > 0 else Fore.WHITE + 'N/A'}")


        print(Fore.CYAN + "=" * 60)
        print("LIST: ")
        print()

        # Print out list items
        for key, value in self.todo_list.items():
            if value[1]:
                print(Fore.GREEN + f" ◉ {key:<3}" + Fore.WHITE + f"➱ {value[0]:<25} " + Fore.GREEN + "✓" + Fore.WHITE)
            else:
                print(Fore.RED + f" ◉ {key:<3}" + Fore.WHITE + f"➱ {value[0]:<25} " + Fore.RED + "✗" + Fore.WHITE)

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
        print(Fore.CYAN + "[TODO: " + list_name + "] " + "Available commands: " + Fore.YELLOW + "add [task], del [task], com [task no], uncom [task no] , view, help, back" + Fore.RESET)
        list_instance = global_lists[list_name]
        while True:
            action = input(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.YELLOW  + ">> ")
            parsed = action.split(" ")
            if parsed[0] == "add":
                    list_instance.todo_list[str(len(list_instance.todo_list)+1)] = [''.join(parsed[1:]), False]
                    print(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.MAGENTA + "Task \"" + ' '.join(parsed[1:]) + "\" has been added to the list!" + Fore.RESET)

            elif parsed[0] == "help":
                print(Fore.CYAN + "[TODO: " + list_name + "] " + "Available commands: " + Fore.YELLOW + "add [task], del [task], com [task no], uncom [task no], view, help, back" + Fore.RESET)

            elif parsed[0] == "com":
                    try:
                        list_instance.complete(parsed[1])
                        print(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.GREEN + "✓ Task " + parsed[1] + " has been marked as completed!" + Fore.RESET)
                    except:
                        print(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.RED + "✗ ERROR: Task number \"" + parsed[1] + "\" is invalid!" + Fore.RESET)
    

            elif parsed[0] == "uncom":
                    try:
                        list_instance.uncomplete(parsed[1])
                        print(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.RED + "✗ Task " + parsed[1] + " is now marked as uncompleted!" + Fore.RESET)
                    except:
                        print(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.RED + "ERROR: Task number \"" + parsed[1] + "\" is invalid!" + Fore.RESET)
    
            elif parsed[0] == "del":
                    try:
                        list_instance.delete(parsed[1])
                        print(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.RED + "Task " + parsed[1] + " has been deleted from the list!" + Fore.RESET)
                    except:
                        print(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.RED + "ERROR: Task number \"" + parsed[1] + "\" is invalid!" + Fore.RESET)



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
    print(Fore.CYAN + "➪ Delete [list name] - To delete a specific list")
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

    elif parsed[0] == "delete":
        if parsed[1] in global_lists:
            global_lists.pop(parsed[1])
            print()
            print(Fore.MAGENTA + "List \"" + parsed[1] + "\" has been deleted successfully!" + Fore.RESET)
        else:
            print()
            print(Fore.RED + "ERROR: List \"" + parsed[1] + "\" does not exist " + Fore.RESET)


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



      
 



