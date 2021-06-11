import re

print("\nLab 8\nAuthor: Lazarev Dmitry\nGroup: ITb-2302\nVariant 6\n")

#Ex 1
'''
Написать регулярное выражение, определяющее, является ли строка кодом цвета в 16-ричном формате.
Корректные значения:	#03B63A, #FFF, #000
Некорректные значения:	ABCDEF, 123, #GHIJKL
'''
def Ex1():
	print("Задание 1")
	cod_color = input("Введите код цвета: ")
	if len(cod_color) == 7:
		result_cod_color = re.compile(r'#[0-9A-Fa-f]{6}$')
		if result_cod_color.match(cod_color):
			print("Верный код:", cod_color)
		else:
			print("Неверный код:", cod_color)
	elif len(cod_color) == 4:
		result_cod_color = re.compile(r'#[0-9A-Fa-f]{3}$')
		if result_cod_color.match(cod_color):
			print("Верный код:", cod_color)
		else:
			print("Неверный код:", cod_color)
	else:
		print("Введите код цвета заново")
Ex1()
# Ex 6
'''
Написать регулярное выражение, проверяющее номер телефона на соответствие российскому формату.
Номер должен начинаться с +7 или 8, далее в скобках один из кодов: 909, 912, 922, затем цифры
номера через дефис.
'''
def Ex6():
	print ("\nЗадание 6")
	number = input("Введите номер: ")
	result_number = re.compile(r'^(\+7|7|8)?[\s\-]?\(?([0-9]){3}\)?[\s\-]?[0-9]{3}[\s\-]?-[0-9]{2}[\s\-]?-[0-9]{2}$')
	if result_number.match(number):
		print("Введен верный номер: ", number)
	else:
		print("Введен не верный номер: ", number)
Ex6()

# Ex 9
'''
Написать регулярное выражение, проверяющее строку на соответствие почтовому индексу в российском формате.
Корректные значения:	123456
Некорректные значения:	123 456, str123456str, 123a456b
'''
def Ex9():
	print ("\nЗадание 9")
	index = input("Введите почтовый индекс: ")
	result_index = re.compile(r'^\d{6}$')
	if result_index.match(index):
		print("Введен верный номер: ", index)
	else:
		print("Введен не верный номер: ", index)
Ex9()
