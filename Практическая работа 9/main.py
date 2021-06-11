import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QTableWidgetItem, QLineEdit
from phonebook import Ui_PhoneBook

def application():
	app = QApplication(sys.argv)
	#widget=QWidget()
	Visual = QMainWindow()
	GUI = Ui_PhoneBook()
	GUI.setupUi(Visual)

	Visual.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	application()