from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PhoneBook(object):
    def setupUi(self, PhoneBook):
        PhoneBook.setObjectName("PhoneBook")
        PhoneBook.resize(540, 360)
        font = QtGui.QFont()
        font.setPointSize(12)
        PhoneBook.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("source/3709735-application-contact-directory-phonebook-storage_108083.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PhoneBook.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(PhoneBook)
        self.centralwidget.setObjectName("centralwidget")
        self.leName = QtWidgets.QLineEdit(self.centralwidget)
        self.leName.setGeometry(QtCore.QRect(10, 10, 200, 30))
        self.leName.setText("")
        self.leName.setObjectName("leName")
        self.leNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.leNumber.setGeometry(QtCore.QRect(220, 10, 200, 30))
        self.leNumber.setObjectName("leNumber")
        self.Add = QtWidgets.QPushButton(self.centralwidget)
        self.Add.setGeometry(QtCore.QRect(430, 10, 100, 30))
        self.Add.setObjectName("Add")
        self.Add.clicked.connect(self.add_row)
        self.twPhoneBook = QtWidgets.QTableWidget(self.centralwidget)
        self.twPhoneBook.setGeometry(QtCore.QRect(10, 50, 520, 300))
        self.twPhoneBook.setMinimumSize(QtCore.QSize(520, 0))
        self.twPhoneBook.setObjectName("twPhoneBook")
        self.twPhoneBook.setColumnCount(2)
        self.twPhoneBook.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.twPhoneBook.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.twPhoneBook.setHorizontalHeaderItem(1, item)
        self.twPhoneBook.horizontalHeader().setCascadingSectionResizes(False)
        self.twPhoneBook.horizontalHeader().setDefaultSectionSize(250)
        self.twPhoneBook.horizontalHeader().setHighlightSections(False)
        self.twPhoneBook.horizontalHeader().setMinimumSectionSize(50)
        self.twPhoneBook.horizontalHeader().setSortIndicatorShown(False)
        PhoneBook.setCentralWidget(self.centralwidget)

        self.retranslateUi(PhoneBook)
        QtCore.QMetaObject.connectSlotsByName(PhoneBook)

    def retranslateUi(self, PhoneBook):
        _translate = QtCore.QCoreApplication.translate
        PhoneBook.setWindowTitle(_translate("PhoneBook", "Телефонный справочник"))
        self.leName.setPlaceholderText(_translate("PhoneBook", "Имя"))
        self.leNumber.setInputMask(_translate("PhoneBook", "8(999)999-99-99  "))
        self.leNumber.setText(_translate("PhoneBook", "8()--  "))
        self.Add.setText(_translate("PhoneBook", "Добавить"))
        item = self.twPhoneBook.horizontalHeaderItem(0)
        item.setText(_translate("PhoneBook", "Имя"))
        item = self.twPhoneBook.horizontalHeaderItem(1)
        item.setText(_translate("PhoneBook", "Номер телефона"))

    def add_row(self):
        name = self.leName.text()
        number = self.leNumber.text()

        rowPosition = self.twPhoneBook.rowCount()
        self.twPhoneBook.insertRow(rowPosition)

        #Add text in table
        self.twPhoneBook.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(name))
        self.twPhoneBook.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(number))

        self.leName.clear()
        self.leNumber.clear()
