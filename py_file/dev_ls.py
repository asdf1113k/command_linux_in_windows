import os
import sys
from colorama import init, Fore, Back, Style
# from tabulate import tabulate # либа для таблиц не импортируется !!!


def view_dir_or_file():

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
        # print(list_dirs)
    except PermissionError:
        print(Fore.LIGHTRED_EX + "command ls: Permission denied")# в доступе отказано
        print(Fore.LIGHTGREEN_EX + "using command 'dir'")
        os.system("dir")
        sys.exit()
    except ValueError:
        sys.exit()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!! раскрашивание папок и файлов и вывод их в терминал !!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for dir in list_dirs:
        if "." in dir[:1]:  # dir hidden
            print(Fore.CYAN + dir, end=" | ")
        else: # dir
            print(Fore.BLUE + dir, end=" | ")
    else:
        print(end="\n")

    for file in list_files:
        if "." in file[:1]: # file hidden
            print(Back.CYAN + file, end=" | ")
        else:
            print(Fore.WHITE + file, end=" | ")
    else:
        print(end="\n")

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!! просмотр содержимого указанной директории  !!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # print(sys.argv[1])
    # if "\\" in sys.argv[1]:
    #     os.listdir((sys.argv[1]))


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!! просто по приколу. Надо будет не забыть убрать !!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if "dead" in sys.argv:
        os.system('color 4')
        os.system('dir /s')

if __name__ == '__main__':
    view_dir_or_file()