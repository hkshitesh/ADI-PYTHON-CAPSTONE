import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton

app = QApplication(sys.argv)

window = QWidget()

d = QDial(window)
d.move(50,50)
d.setWindowTitle("Dialer")

s = QSlider(window)
s.move(300,50)

button = QPushButton(window, text = 'Reset')
button.move(200,300)

def Reset_slider():
    s.setValue(50)

button.clicked.connect(Reset_slider)
s.valueChanged.connect(d.setValue)
d.valueChanged.connect(s.setValue)

window.show()
app.exec_()
