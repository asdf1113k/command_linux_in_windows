# description
набор батников(*.bat файлов) которые называются как команды в linux, которые просто запускают команды PowerShell

# install
/*не проверял это на windows но обязательно проверю*/
```bash
git clone https://github.com/asdf1113k/command_linux_in_windows.git
```
дальше нужно прописать путь к папке comand_linux_in_windows в переменной PATh

```
setx /M path "%path%;C:\ваш\путь\до\папки\command_linux_in_windows"
```

# TODO:
убрать зависимость от ЯП python, сделать на ЯП bat

сделать возможность указывать аргументы, скорее всего это будет обычный if else в каждом файле, потом обязательно подумать как это можно улучшить оптимизироваать и тп

добавить команды ifconfig, hexdump и посмотреть в интернете стандартные команды Linux
