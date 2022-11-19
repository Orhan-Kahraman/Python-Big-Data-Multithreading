import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from csv_file_parsing import *
from helper_func import *


class app_window(QWidget):

    def __init__(self, parent=None):
        super(app_window, self).__init__(parent)
        self.setGeometry(700, 300, 700, 500)
        self.setWindowTitle("Sorter")
        self.setWindowIcon(QIcon("assets/shortcut.png"))
        self.setToolTip("Sorter")
        self.uidesign()

    def uidesign(self):
        # Datadaki column isimlerini almak
        columnNames = csvSett.get_column_names()

        # Kutulara maksimum değerlerini vermek
        validator = QIntValidator(bottom=0, top=100, parent=self)

        # Etiketleri oluşturmak
        self.item1 = QtWidgets.QLabel(self, text=columnNames[0])
        self.item2 = QtWidgets.QLabel(self, text=columnNames[1])
        self.item3 = QtWidgets.QLabel(self, text=columnNames[2])
        self.item4 = QtWidgets.QLabel(self, text=columnNames[3])
        self.item5 = QtWidgets.QLabel(self, text=columnNames[4])
        self.item6 = QtWidgets.QLabel(self, text=columnNames[5])
        self.threadNum = QtWidgets.QLabel(self, text="Thread Sayısı")

        # İnput girişlerini oluşturmak
        self.additem1 = QtWidgets.QLineEdit(self)
        self.additem2 = QtWidgets.QLineEdit(self)
        self.additem3 = QtWidgets.QLineEdit(self)
        self.additem4 = QtWidgets.QLineEdit(self)
        self.additem5 = QtWidgets.QLineEdit(self)
        self.additem6 = QtWidgets.QLineEdit(self)
        self.addthreadNum = QtWidgets.QLineEdit(self)

        # Valiidator değerlerini inputlara atamak
        self.additem1.setValidator(validator)
        self.additem2.setValidator(validator)
        self.additem3.setValidator(validator)
        self.additem4.setValidator(validator)
        self.additem5.setValidator(validator)
        self.additem6.setValidator(validator)

        # Maksimum sayının 100 olmasını sağlamak
        self.additem1.cursorPositionChanged.connect(
            lambda: check_input(self.additem1.text(), self.additem1))
        self.additem2.cursorPositionChanged.connect(
            lambda: check_input(self.additem2.text(), self.additem2))
        self.additem3.cursorPositionChanged.connect(
            lambda: check_input(self.additem3.text(), self.additem3))
        self.additem4.cursorPositionChanged.connect(
            lambda: check_input(self.additem4.text(), self.additem4))
        self.additem5.cursorPositionChanged.connect(
            lambda: check_input(self.additem5.text(), self.additem5))
        self.additem6.cursorPositionChanged.connect(
            lambda: check_input(self.additem6.text(), self.additem6))

        # Thread EKSİK!!!

        # Uygulama butonu
        self.myBut = QtWidgets.QPushButton(text="Uygula")
        self.myBut.clicked.connect(lambda: add_percentage(additem1=self.additem1, additem2=self.additem2,
                                   additem3=self.additem3, additem4=self.additem4, additem5=self.additem5, additem6=self.additem6))

        # Widgetları düzenlemek
        fbox = QtWidgets.QFormLayout()

        fbox.addRow(self.item1, self.additem1)
        fbox.addRow(self.item2, self.additem2)
        fbox.addRow(self.item3, self.additem3)
        fbox.addRow(self.item4, self.additem4)
        fbox.addRow(self.item5, self.additem5)
        fbox.addRow(self.item6, self.additem6)
        fbox.addRow(self.threadNum, self.addthreadNum)

        fbox.addRow(self.myBut)

        self.setLayout(fbox)


def window():
    # Uygulamayı çizdirme fonksiyonu
    app = QApplication(sys.argv)
    win = app_window()
    win.show()
    csvSett.use_new_rows()
    sys.exit(app.exec_())


csvSett = CsvSettings()

window()
