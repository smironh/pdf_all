from art import tprint
from pathlib import Path

import results

def main():
	tprint('all pdf')
	print('''
1)pdf >> txt
2)pdf >> mp3
3)pdf >> html
4)pdf >> docx
''')

	all_convert = [1, 2, 3, 4]

	number = input('Введите что хотите запустить > ')
	if int(number) in all_convert:
		path = input('Введите путь .pdf файла > ')
		if int(number) == 1:
			if Path(path).is_file() and Path(path).suffix == '.pdf':

				results.pdf_to_txt(path)
			else:
				print('Ошибка! Не найден путь к .pdf файлу!')
		elif int(number) == 2:
			if Path(path).is_file() and Path(path).suffix == '.pdf':

				language = input("Выберете язык, пример: 'en' или 'ru': ")
				while language not in ("en", "ru"):
					language = input("Выберете язык, пример: 'en' или 'ru':  ")
				print(results.pdf_to_mp3(file_path=path, language=language))
			else:
				print('Ошибка! Не найден путь к .pdf файлу!')
		elif int(number) == 3:
			if Path(path).is_file() and Path(path).suffix == '.pdf':
				results.pdf_to_html(path)
			else:
				print('Ошибка! Не найден путь к .pdf файлу!')
		elif int(number) == 4:
			if Path(path).is_file() and Path(path).suffix == '.pdf':
				results.pdf_to_docx(path)
			else:
				print('Ошибка! Не найден путь к .pdf файлу!')
		else:
			print('Ошибка! такой функции нет!')
	else:
		print('Ошибка! Введите корректную цифру')



if __name__ == '__main__':
	main()
