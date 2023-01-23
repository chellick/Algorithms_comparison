# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         button = QPushButton("Press Me!")
#         button.setCheckable(True)
#         button.clicked.connect(self.the_button_was_clicked)
#         button.clicked.connect(self.the_button_was_toggled)
#
#         self.setCentralWidget(button)
#
#     def the_button_was_clicked(self):
#         print("Clicked!")
#
#     def the_button_was_toggled(self, checked):
#         print("Checked?", checked)
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()


import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
from PyQt5 import QtWidgets
import designGA  # Это наш конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow, designGA.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна


