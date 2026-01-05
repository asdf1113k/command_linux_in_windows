import os
import sys
from colorama import init, Fore, Back, Style
init()  # или init(autoreset=True)

# os.system('dir') # старый вывод папок и файлов


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