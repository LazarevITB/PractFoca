import numpy as np
import random as r

# Author
print("\nLab 2\nAuthor: Lazarev Dmitry\nGroup: ITb-2302\nVariant 6\n")

# Ex 3
'''
Написать функцию,выполняющую циклический
сдвиг элементов массива на указанное число элемен-тов.
'''

print("Ex 3\n")
# Переменные 
length = int(input("Length array? ")) #Длинна массива

#Массив (заполнение через рандом)
array = [r.randint(1,10) for i in range(length)]
print("Initial array:", array )

shift = int(input("How much to move? ")) #То насколько ты хочешь сдвинуть

#Функция сдвига
array = array[-shift:] + array[:-shift]

print("Array after offset:", array)

# Ex 6
'''
Задание: Написать функцию, которая для заданной квадратной матрицы
целых чисел находит сумму элементов на главной диагонали
'''

print("\nEx 6\n")

length_matrix = 3 #Длинна матрицы
print("Length matrix:", length_matrix)
#Заполнение матрицы
matrix = [[r.randint(1,10) for i in range(length_matrix)],[r.randint(1,10) for i in range(length_matrix)],[r.randint(1,10) for i in range(length_matrix)]]
print("Initial matrix:",matrix)
#Сумма главной диагонали
sum_main_diagonal = sum(matrix[i][i] for i in range(length_matrix))
print("Summa main diagonal =", sum_main_diagonal)

# Ex 8
'''
Написать функцию, которая получает 3-значное число и
возвращает строку, содержащее это число, описанное словами. 
'''

print("\nEx 8\n")

# Сотни
hund = {0: '', 1: 'one_hundred', 2: 'two_hundred', 3: 'three_hundred', 4: 'four_hundred', 
		5: 'five_hundred', 6: 'six_hundred', 7: 'seven_hundred', 8: 'eight_hundred', 9: 'nine_hundred'}
# Десятки
dec = {0: '', 1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty', 
		5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
# Еденицы
one = {0: 'zero', 1: 'one', 2: 'two', 3: 'threere', 4: 'four', 
		5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

# print("Enter number for 0 to 999:")
def Convert_number_in_text(hund, dec, one):
	h = int(input("Enter hund: ")) # Ввод сотен
	d = int(input("Enter dec: ")) # Ввод десятков
	o = int(input("Enter one: ")) # Ввод едениц

	print("Your number converted to text: ", '%s %s %s' % (hund[h], dec[d], one[o])) # Вывод

Convert_number_in_text(hund, dec, one) # Вызов функции


