
import datetime
import json
import colorama 
from colorama import Fore, Back, Style
import time
import os
from groq import Groq
from dotenv import load_dotenv


# Configure Groq API key
load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    print(Fore.YELLOW + "No Groq API key found!" + Fore.RESET)
    print(Fore.YELLOW + "You would need one to use TOODLES, our AI-powered todo assistant!" + Fore.RESET)
    key = input(Fore.YELLOW + "Enter your Groq API key (get one free at console.groq.com): " + Fore.RESET)
    with open(".env", "w") as f:
        f.write(f"GROQ_API_KEY={key}")
    os.environ["GROQ_API_KEY"] = key
    print(Fore.GREEN + "Key saved! You won't be asked again." + Fore.RESET)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

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
    def __init__(self,name, time = None, list = None):
        self.list_name = name
        self.date = time or datetime.datetime.now()
        self.todo_list = list or {}
    
    def complete(self,num):
        self.todo_list[num][1] = True 

    def uncomplete(self,num):
        self.todo_list[num][1] = False 

    def delete(self,num):
        self.todo_list.pop(num)

    def print_list(self):
        # showcase list
        print()
        print(Fore.CYAN + "=" * 60)
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
        print(Fore.CYAN + "=" * 60)

        print()
   

# List Creation Functions in the main page 
def create_list(list_name):
    print()    
    if list_name not in global_lists:
        list_object = todo(list_name)
        global_lists[list_name] = list_object
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
        print(Fore.RED + "=" * 60 + "   ")
        print(Fore.RED + "New Feature: " +  Fore.WHITE + "Use the power of TOODLE! Your personal todo helper. Type " + Fore.RED + "\"do [instruction]\"" + Fore.WHITE + " to let AI manage your list")
        print(Fore.RED + "AI Tip: "       + Fore.WHITE + "Ask AI questions with " + Fore.RED + "\"do tell [question]\"" + Fore.WHITE + " to query your list!" + Fore.RESET)
        print(Fore.RED + "AI Tip: "       + Fore.WHITE + "Rearange list with " + Fore.RED + "\"do order [query]\"" + Fore.WHITE + " to sort your list" + Fore.RESET)
        print(Fore.RED + "=" * 60 + "   ")

        print()
        print(Fore.CYAN + "[TODO: " + list_name + "] " + "Available commands: " + Fore.YELLOW + "add [task], del [task], com [task no], uncom [task no] , view, help, back" + Fore.RESET)

        list_instance = global_lists[list_name]
        while True:
            action = input(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.YELLOW  + ">> ")
            parsed = action.split(" ")

            if parsed[0] == "do" or parsed[0] == "Do":
                do_ai(parsed[1:], list_name, list_instance.todo_list)

            elif parsed[0] == "add" or parsed[0] == "Add":
                    list_instance.todo_list[str(len(list_instance.todo_list)+1)] = [" ".join(parsed[1:]), False]
                    print(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.MAGENTA + "Task \"" + ' '.join(parsed[1:]) + "\" has been added to the list!" + Fore.RESET)

            elif parsed[0] == "help" or parsed[0] == "Help":
                print(Fore.CYAN + "[TODO: " + list_name + "] " + "Available commands: " + Fore.YELLOW + "add [task], del [task], com [task no], uncom [task no], view, help, back" + Fore.RESET)

            elif parsed[0] == "com" or parsed[0] == "Com" or parsed[0] == "check" or parsed[0] == "Check" or parsed[0] == "complete" or parsed[0] == "Complete" or parsed[0] == "tick" or parsed[0] == "Tick":
                    try:
                        list_instance.complete(parsed[1])
                        print(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.GREEN + "✓ Task " + parsed[1] + " has been marked as completed!" + Fore.RESET)
                    except:
                        print(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.RED + "✗ ERROR: Task number is invalid!" + Fore.RESET)
    

            elif parsed[0] == "uncom" or parsed[0] == "Uncom" or parsed[0] == "uncheck" or parsed[0] == "Uncheck" or parsed[0] == "uncomplete" or parsed[0] == "Uncomplete" or parsed[0] == "untick" or parsed[0] == "Untick":
                    try:
                        list_instance.uncomplete(parsed[1])
                        print(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.RED + "✗ Task " + parsed[1] + " is now marked as uncompleted!" + Fore.RESET)
                    except:
                        print(Fore.CYAN + "[TODO: " + list_name + "] " + Fore.RED + "ERROR: Task number is invalid!" + Fore.RESET)
    
            elif parsed[0] == "del" or parsed[0] == "Del" or parsed[0] == "delete" or parsed[0] == "Delete":

                    try:
                        list_instance.delete(parsed[1])

                        # renumber tasks
                        new_list = {}
                        i = 1
                        for key, value in list_instance.todo_list.items():
                            new_list[str(i)] = value
                            i += 1
                        list_instance.todo_list = new_list

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


def do_ai(instruction, list_name, current):

    rearrange_triggers = ["rearrange", "rearange", "reorder", "re-order", "sort", "prioritise", "prioritize","order","arange"]

    if any(word in " ".join([x.lower() for x in instruction]) for word in rearrange_triggers):
        prompt = f"""
        You are reordering a to-do list. Return ONLY a JSON array of task names in the new order. Nothing else.
        YOU WILL KEEP the completion status of each task.

        Current list:
        {current}

        Instruction: {instruction}

        Rules:
        - Keep completed tasks at the top, only reorder uncompleted ones
        - Return ALL task names, none missing - you will add tick boxes next to each to show completion status
        - Return ONLY a JSON array like: ["Task A [✓]", "Task B [x]", "Task C [x]"]
        """
    else:
        prompt = f"""
        You are a silent executor for a terminal to-do list app called PyDo.
        You return ONLY a valid JSON object with two fields. No explanation. No markdown. Nothing else. Unless the user is asking a question about the data via "do tell" command, then you can answer in a single line if possible,but appropriate you can answer more if it furfills the users question, but still return an empty command list.

        List name: {list_name}
        Current list:
        {current if current else "empty"}

        Available commands:
        - "add [task name]"
        - "del [task number]"
        - "com [task number]"
        - "uncom [task number]"
        - "tell [user asking about the list or its data]"

        Rules:
        - Return ONLY a valid JSON object, nothing else
        - Each "add" command must have a full meaningful task name, NEVER split words into separate commands
        - "add top 10 rappers" means generate 10 actual rapper names, one per command
        - "commands" must be complete and thorough — never be lazy, if asked for 10 return 10
        - "message" must be a single ultra short line describing what you did, max 6 words
        - EXCEPTION: if the instruction starts with "tell", the "message" can be as long as needed to properly answer the question — be genuinely helpful, give real information, not just 2 words
            - For "tell" queries, treat message as a full answer. Example: "do tell me what I can cook with these ingredients" should return a real helpful response listing ideas, not just "Here are ideas"
            - For "tell" queries about the list data, use your own knowledge too — if the list has Palestine cities, you can talk about what to do there, history, food, etc.
            - For "tell" queries, it must be about the data in the list, or the list itself — never answer general questions that are not related to the list or its data 
            - Your personality for tell queries should be of a nonchalant friend who is an expert on the list topic — for example if the list is about rappers, you are a friend who knows a lot about rap and can give great insights in a chill way
        - Be smart — "complete rapper tasks" means only complete tasks that are rapper names
        - For ingredients, add each one as a separate task with its full name
        - Generate real, varied, specific names — never generic placeholders
        - For deletes, there is a logic where when a task is deleted, the list renumbers itself, so be mindful of that when deleting multiple tasks - if you delete task 2 and then task 5, the original task 5 is now task 4 after the first delete, so you should delete task 4 in the second command, not task 5 - be smart about the order of your commands to avoid this issue
        - When asked to delete all tasks, generate commands to delete each task one by one, starting from the highest number task down to 1, to avoid the renumbering issue, dont forget to delete task 1 at the end
        - "remove all except X" means ONLY delete tasks that are NOT X, keep X in the list
        - Before deleting, figure out which tasks to KEEP, then delete everything else
        - Double check your commands — if asked to keep Drake, Cole and Travis, those task numbers must NOT appear in your del commands
        - ONLY say "I don't understand" if the instruction is total gibberish or completely impossible to execute
        - If the instruction makes any sense at all, just do your best and execute it
        - "add ingredients for chicken curry" = totally valid, add the ingredients
        - Never refuse a reasonable instruction, always attempt it
        - if the user says "tell" it is a conversational query BUT it must be 100% related to the actual items in the list — if the list has rappers, you can only answer questions about those specific rappers, nothing else
        - if the tell query has nothing to do with the list data, respond with "bro that's not on the list" and return empty commands
        - NEVER answer general knowledge questions that aren't directly about the list items — "who is allah" when the list has rappers = not relevant, shut it down
        - your personality for tell queries is a nonchalant friend who knows their stuff — no formal language, no "I", talk like a real person. Example: "God's Plan goes hard but honestly Marvin's Room is the real one" not "Drake's best song is God's Plan"

        Example:
        - User says: "remove all except Drake and Cole" (list has: 1:Drake, 2:Kanye, 3:Cole, 4:Travis)
        - WRONG: ["del 4", "del 3", "del 2", "del 1"]
        - CORRECT: ["del 4", "del 2"]  (only delete Kanye and Travis, keep Drake and Cole)

        Example:
        User says: "add top 5 rappers"
        WRONG: ["add top", "add 5", "add rappers"]
        CORRECT: ["add Drake", "add Kendrick Lamar", "add J Cole", "add Travis Scott", "add Tyler the Creator"]

        Return format:

        FOR ALL INSTRUCTIONS EXCEPT "tell" and "rearange":
        {{"message": "brief message here", "commands": ["add Drake", "add Kendrick Lamar"]}}

        User instruction: {instruction}

        Return format:
        {{"message": "brief message here", "commands": ["add eggs", "add potatoes", "com 1"]}}
        """

    try:
        # Models we can try
        # llama-3.3-70b-versatile — what you're using, smartest but burns tokens fast (original)
        # llama-3.1-8b-instant — way smaller, uses way fewer tokens, still solid for simple tasks

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
    except Exception as e:
        print(Fore.RED + "ERROR: AI request failed - " + repr(e) + Fore.RESET)
        return

    # Return varies depending on if its set of instructions (returns message and commands) or rearranging (returns just the new order in a list)
    raw = response.choices[0].message.content.strip()
    try:
        data = json.loads(raw)
    except:
        # Assign returned list, its not a JSON object but a plain list of the new order of tasks
        start = raw.find("[")
        end = raw.rfind("]") + 1
        data = json.loads(raw[start:end])
        
    # If the response is a list, its a rearranging instruction 
    if isinstance(data, list):

        global_lists[list_name].todo_list = {}
        
        for item in data:
            start = item.find("[")
            end = item.rfind("]") + 1
            com = item[start:end]
            task = item[:start].strip()
            status = True if com == "[✓]" else False
            global_lists[list_name].todo_list[str(len(global_lists[list_name].todo_list)+1)] = [task, status]

        return

    # Otherwise, its a normal instruction with message and commands

    message = data["message"]
    actions = data["commands"]

    # Extract commands and message from response
    response.choices[0].message.content
    print(Fore.RED + "[TOODLE: " + list_name + "] " + Fore.WHITE + message + Fore.RESET)

    # Execute commands
    list_instance = global_lists[list_name]
    for action in actions:
        parsed = action.split(" ")
        if parsed[0] == "add":
            list_instance.todo_list[str(len(list_instance.todo_list)+1)] = [" ".join(parsed[1:]), False]
            print(Fore.RED + "[TOODLE: " + list_name + "] " + Fore.MAGENTA + "Task \"" + ' '.join(parsed[1:]) + "\" has been added to the list!" + Fore.RESET)

        elif parsed[0] == "com":
            try:
                list_instance.complete(parsed[1])
                print(Fore.RED + "[TOODLE: " + list_name + "] " + Fore.GREEN + "✓ Task " + parsed[1] + " has been marked as completed!" + Fore.RESET)
            except:
                print(Fore.RED + "[TOODLE: " + list_name + "] " + Fore.RED + "✗ ERROR: Task number is invalid!" + Fore.RESET)

        elif parsed[0] == "uncom":
            try:
                list_instance.uncomplete(parsed[1])
                print(Fore.RED + "[TOODLE: " + list_name + "] " + Fore.RED + "✗ Task " + parsed[1] + " is now marked as uncompleted!" + Fore.RESET)
            except:
                print(Fore.RED + "[TOODLE: " + list_name + "] " + Fore.RED + "ERROR: Task number is invalid!" + Fore.RESET)

        elif parsed[0] == "del":
            try:
                list_instance.delete(parsed[1])

                # renumber tasks
                new_list = {}
                i = 1
                for key, value in list_instance.todo_list.items():
                    new_list[str(i)] = value
                    i += 1
                list_instance.todo_list = new_list

                print(Fore.RED + "[TOODLE: " + list_name + "] " + Fore.RED + "Task " + parsed[1] + " has been deleted from the list!" + Fore.RESET)
            except:
                print(Fore.RED + "[TOODLE: " + list_name + "] " + Fore.RED + "ERROR: Task number \"" + parsed[1] +"\" is invalid!"  + Fore.RESET)
        




    
                    
# Lists out all commands possible 
def list_help():
    print()
    print(Fore.CYAN + "=" * 60)
    print("Available commands:")
    print(Fore.CYAN + "➪ Create [list name] - Create a new to-do list with the specified name")
    print(Fore.CYAN + "➪ Select [list name] - To view a specific list")
    print(Fore.CYAN + "➪ Delete [list name] - To delete a specific list")
    print(Fore.CYAN + "➪ View - View all lists")
    print(Fore.CYAN + "➪ Api -  Change AI API keyto use TOODLE(get a free one at console.groq.com)")
    print(Fore.CYAN + "➪ Exit - Exit the program")
    print()
    print(Fore.CYAN + "=" * 60)



# START - Load Save if it exists
try:

    with open('pydosave.txt', 'r+') as file:

        choice = input(Fore.YELLOW + "Load save? (Y/N): ")
        if choice == "y" or choice == "Y":  
            data = json.load(file)
            # Re populate the global list
            for name, todoitem in data.items():
                global_lists[name] = todo(
                todoitem["list_name"],
                datetime.datetime.fromisoformat(todoitem["date"]),
                todoitem["todo_list"]
            )
            print(Fore.YELLOW + "Save file loaded successfully!" + Fore.RESET)
        else:
            file.seek(0)
            file.truncate()
            print(Fore.YELLOW + "Starting a new session..." + Fore.RESET)

except:
    print(Fore.RED + "Could not load save file") 
    pass


print()
list_help()
print()

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

    elif parsed[0] == "create" or parsed[0] == "Create":
        if parsed[1].strip() == "":
            print()
            print(Fore.RED + "ERROR: List name cannot be empty" + Fore.RESET)
        else:
            create_list(" ".join(parsed[1:]).strip())
        
    elif parsed[0] == "view" or parsed[0] == "View":
        view_lists()

    elif parsed[0] == "select" or parsed[0] == "Select":
        select_list(parsed[1])

    elif parsed[0] == "help" or parsed[0] == "Help":
        list_help()

    elif parsed[0] == "delete" or parsed[0] == "Delete":
        if parsed[1] in global_lists:
            global_lists.pop(parsed[1])
            print()
            print(Fore.MAGENTA + "List \"" + parsed[1] + "\" has been deleted successfully!" + Fore.RESET)
        else:
            print()
            print(Fore.RED + "ERROR: List \"" + parsed[1] + "\" does not exist " + Fore.RESET)
    
    elif parsed[0] == "api" or parsed[0] == "Api":
        print()
        key = input(Fore.YELLOW + "Enter your Groq API key (get one free at console.groq.com): " + Fore.RESET)
        with open(".env", "w") as f:
            f.write(f"GROQ_API_KEY={key}")
        os.environ["GROQ_API_KEY"] = key
        client = Groq(api_key=key)
        print(Fore.GREEN + "Key saved and loaded! Good to go." + Fore.RESET)


        # End program
    elif parsed[0] == "exit" or parsed[0] == "Exit":
        print()
        print(Fore.MAGENTA + "Saving todo's.....")
        time.sleep(1.5)

        # Make the dumps of the global lists
        dump = {}
        for key, todoitem in global_lists.items():
            dump[key] = {
                "list_name": todoitem.list_name,
                "date": todoitem.date,
                "todo_list": todoitem.todo_list
            }

        # Lets overwrite and create the save file
        with open("pydosave.txt", "w+") as f:
            json.dump(dump, f, indent=4, sort_keys=True, default=str)


        print()
        time.sleep(1.5)
        print(Fore.MAGENTA + "Exiting PyDo..." + Fore.RESET)
        break


    else:
        print()
        print(Fore.RED  + "ERROR: Command \"" + command + "\" is invalid")

# Exit Screen
time.sleep(1.5)
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



      
 



