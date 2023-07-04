from art import tprint
from pathlib import Path

import results

def main():
	tprint('all pdf')
	print('''
1)pdf >> txt
2)pdf >> mp3
''')

	all_convert = [1, 2]

	number = input('Введите что хотите запустить > ')
	if int(number) in all_convert:
		path = input('Введите путь .pdf файла > ')
		if int(number) == 1:
			if Path(path).is_file() and Path(path).suffix == '.pdf':

				results.pdf_to_txt(path)
			else:
				print('Ошибка! Не найдет путь к .pdf файлу!')
		elif int(number) == 2:
			language = input("Выберете язык, пример: 'en' или 'ru': ")
			while language not in ("en", "ru"):
				language = input("Выберете язык, пример: 'en' или 'ru':  ")
			print(results.pdf_to_mp3(file_path=path, language=language))
		else:
			print('Ошибка! такой функции нет!')
	else:
		print('Ошибка! Введите корректную цифру')



if __name__ == '__main__':
	main()