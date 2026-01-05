import os
import getpass


print("сортировка файлов")

USER_NAME = getpass.getuser() # запрашиваю userName
print(USER_NAME)
os.chdir(f"C:\\Users\\{USER_NAME}\\Downloads") # перехожу в папку загрузок
path_to_directory_downloads = os.getcwd() # возвращаю полный путь до папки с загрузками
all_files = os.listdir()
print(path_to_directory_downloads)

for file in all_files:
    print(file)
    if file[-4:] in [".png", ".jpg", "jfif"]:
        os.replace(f"{path_to_directory_downloads}\\{file}", f"C:\\Users\\{USER_NAME}\\Pictures\\{file}")
    if file[-4:] in [".gif", ".mp4"]:
        os.replace(f"{path_to_directory_downloads}\\{file}", f"C:\\Users\\{USER_NAME}\\Videos\\{file}")
    if file[-4:] in [".wav", ".mp3", ".mp2"]:
        os.replace(f"{path_to_directory_downloads}\\{file}", f"C:\\Users\\{USER_NAME}\\Music\\{file}")

