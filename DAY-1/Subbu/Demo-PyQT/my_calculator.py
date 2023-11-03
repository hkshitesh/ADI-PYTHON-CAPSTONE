import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.input_num1 = QLineEdit(self)
        self.input_num2 = QLineEdit(self)
        self.button_add = QPushButton('Add', self)
        self.button_sub = QPushButton('Subtract', self)
        self.button_mul = QPushButton('Multiply', self)
        self.button_div = QPushButton('Divide', self)
        self.label_result = QLabel('Result', self)

        input_layout = QVBoxLayout()
        input_layout.addWidget(self.input_num1)
        input_layout.addWidget(self.input_num2)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.button_add)
        button_layout.addWidget(self.button_sub)
        button_layout.addWidget(self.button_mul)
        button_layout.addWidget(self.button_div)

        main_layout = QHBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.label_result)

        self.setLayout(main_layout)
        self.button_add.clicked.connect(self.add)
        self.button_sub.clicked.connect(self.sub)
        self.button_mul.clicked.connect(self.mul)
        self.button_div.clicked.connect(self.div)

    def add(self):
        input_n1 = float(self.input_num1.text())
        input_n2 = float(self.input_num2.text())
        result = input_n1+input_n2
        self.label_result.setText(f'Result : {result}')

    def sub(self):
        input_n1 = float(self.input_num1.text())
        input_n2 = float(self.input_num2.text())
        result = input_n1-input_n2
        self.label_result.setText(f'Result : {result}')

    def mul(self):
        input_n1 = float(self.input_num1.text())
        input_n2 = float(self.input_num2.text())
        result = input_n1*input_n2
        self.label_result.setText(f'Result : {result}')

    def div(self):
        input_n1 = float(self.input_num1.text())
        input_n2 = float(self.input_num2.text())
        result = input_n1/input_n2
        self.label_result.setText(f'Result : {result}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mycalc = CalculatorApp()
    mycalc.setWindowTitle("My Calculator")
    mycalc.show()
    sys.exit(app.exec_())
