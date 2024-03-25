'''
Author:Adam Cohill
Date Written: 07/15/23
Assignment : Write a GUI program that converts
Celsius temperatures to Fahrenheit temperatures.
The user should be able to enter a Celsius temperature,
click a button, then see the equivalent Fahrenheit temperature.
Use the following formula to make the conversion 

'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Temperature Converter")
        self.setGeometry(100, 100, 461, 225)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.label = QLabel("Input Celsius temperature", self.central_widget)
        self.label.setGeometry(10, 20, 171, 31)

        self.line_edit = QLineEdit(self.central_widget)
        self.line_edit.setGeometry(40, 60, 113, 20)

        self.convert_button = QPushButton("Press to Convert", self.central_widget)
        self.convert_button.setGeometry(50, 90, 91, 23)
        self.convert_button.clicked.connect(self.convert_temperature)

        self.result_label = QLabel("Result: ", self.central_widget)
        self.result_label.setGeometry(290, 72, 71, 31)

        self.converted_label = QLabel("Your temperature in Fahrenheit is", self.central_widget)
        self.converted_label.setGeometry(220, 30, 201, 31)

    def convert_temperature(self):
        celsius_temp = float(self.line_edit.text())
        fahrenheit_temp = (celsius_temp * 9/5) + 32
        self.result_label.setText("Result: {:.2f} °F".format(fahrenheit_temp))
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
