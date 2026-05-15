import os
import sys
from colorama import init, Fore, Back, Style
init()  # или init(autoreset=True)

# os.system('dir') # старый вывод папок и файлов

# иницилизация colorama
    init(autoreset=True) # или init()
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!! получение папок и файлов !!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    try:
        list_files = [f for f in os.listdir(".") if os.path.isfile(os.path.join(".", f))]
        list_files.sort()
        list_dirs = [d for d in os.listdir(".") if os.path.isdir(os.path.join(".", d))]
        list_dirs.sort()
    except PermissionError:
        print(Fore.LIGHTRED_EX + "command ls: Permission denied")# в доступе отказано
        print(Fore.LIGHTGREEN_EX + "using command 'dir'")
        os.system("dir")
        sys.exit()
    except ValueError:
        sys.exit()

list_files_and_dir = os.listdir()
for file_or_dir in list_files_and_dir:
    if "." in file_or_dir[:1]: # file or dir hidden
        print(Style.RESET_ALL + Back.MAGENTA + file_or_dir)
    elif "." in file_or_dir[1:]: # file
        print(Style.RESET_ALL + Fore.WHITE + file_or_dir)
    else: # dir
        print(Style.RESET_ALL + Fore.BLUE + file_or_dir)


if "dead" in sys.argv:
    os.system('color 4')
    os.system('dir /s')

if "\\" in sys.argv[:-1]:
    print("it work")
    current_dir = os.getcwd()
    print(current_dir)
    # os.path("") # f"{os.getcwd()}"+"\\"+f"{sys.argv[:-1]}"