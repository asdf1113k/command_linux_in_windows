import os
from colorama import Fore


print("сортировка файлов")
if os.name == "nt":
    USER_NAME = os.environ["USERNAME"] # запрашиваю userName
    print(f"пользователь: {USER_NAME}")
    os.chdir(f"C:\\Users\\{USER_NAME}\\Downloads") # перехожу в папку загрузок
    path_to_directory_downloads = os.getcwd() # возвращаю полный путь до папки с загрузками
    all_files = os.listdir()
    print(f"путь до папки 'загрузки': {path_to_directory_downloads}")

    for file in all_files:
        if file[-4:] in [".png", ".jpg", "jfif", "jpeg"]:
            os.replace(f"{path_to_directory_downloads}\\{file}", f"C:\\Users\\{USER_NAME}\\Pictures\\{file}")
            print(f"{file} - отправлен в папку 'Pictures'")
        if file[-4:] in [".gif", ".mp4"]:
            os.replace(f"{path_to_directory_downloads}\\{file}", f"C:\\Users\\{USER_NAME}\\Videos\\{file}")
            print(f"{file} - отправлен в папку 'Videos'")
        if file[-4:] in [".wav", ".mp3", ".mp2"]:
            os.replace(f"{path_to_directory_downloads}\\{file}", f"C:\\Users\\{USER_NAME}\\Music\\{file}")
            print(f"{file} - отправлен в папку 'Music'")
    else:
        print(Fore.LIGHTGREEN_EX + "работа завершена!!!")

if "posix" == "posix":
     USER_NAME = os.environ["USERNAME"]
     print(USER_NAME)