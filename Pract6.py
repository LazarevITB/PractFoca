import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Заголовок
print ("\nLab 6\nAuthor: Lazarev Dmitry\nGroup: ITb-2302\nVariant 3\n")

'''
Исследовать различные варианты полиномов: второй, третьей, четвёртой, пятой степеней.
Для каждого из вариантов построить кривую регрессии и отобразить на одном графике вместе с реальными значениями.
'''

def Polynom():
	x = np.linspace(-3, 3, 201)
	# 2-я степень
	plt.plot(x, x ** 2, color = 'b', linestyle = '--')
	# 3-я степень
	plt.plot(x, x ** 3, color = 'g', linestyle = '-.')
	# 4-я степень
	plt.plot(x, x ** 4, color = 'r', linestyle = ':')
	# 5-я степень
	plt.plot(x, x ** 5, color = 'y', linestyle = '-')
	plt.title('График полинома', fontsize=15)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.axis('tight')
	plt.ylim(-30, 30)
	plt.grid(True)
	plt.show()
Polynom()
