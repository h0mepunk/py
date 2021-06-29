import os
import sys
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def create_dir(dir_name):
	if not dir_name:
		print("Необходимо указать название директории")
		return
	dir_path = os.path.join(os.getcwd(), dir_name)
	print(dir_path)
	try:
		os.mkdir(dir_path)
		print(" {} успешно создана".format(dir_name))
	except FileExistsError:
		print("Такая папка {} есть уже".format(dir_name))


def remove_dir(dir_name):
	if not dir_name:
		print("Необходимо указать название директории")
		input(dir_name)
		return
	dir_path = os.path.join(os.getcwd(), dir_name)
	print(dir_path)
	os.rmdir(dir_path)
	print(" {} успешно удалена".format(dir_name))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def show_dir():
	print("Текущая директория:", os.getcwd())
	return os.getcwd()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def file_copy():
	dir_path_1 = os.getcwd() + "/" + sys.argv[0]
	dir_path_1 = dir_path_1.replace(".py", "_copy.py")
	with open(dir_path_1, 'w', encoding="UTF-8") as cp_file:
		with open(sys.argv[0], 'r', encoding="UTF-8") as f:
			for line in f:
				cp_file.write(line)
	with open(dir_path_1, 'r', encoding="UTF-8") as f1:
		print(f1.readlines())


if __name__ == "__main__":
	for i in range(1, 9):
		dir_name = "dir_" + str(i)
		create_dir(dir_name)
	for i in range(1, 9):
		dir_name = "dir_" + str(i)
		remove_dir(dir_name)
	show_dir()
	file_copy()
