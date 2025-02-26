import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QGridLayout, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")
        layout = QVBoxLayout()
        self.result_field = QLineEdit()
        layout.addWidget(self.result_field)

        grid = QGridLayout()

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0)  # Buton pentru Clear
        ]

        for (text, row, col) in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.btn)
            grid.addWidget(button, row, col)

        layout.addLayout(grid)
        self.setLayout(layout)

    def btn(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = str(eval(self.result_field.text()))
                self.result_field.setText(result)
            except Exception:
                self.result_field.setText('Error')
        elif text == 'C':
            self.result_field.clear()
        else:
            self.result_field.setText(self.result_field.text() + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec_())
