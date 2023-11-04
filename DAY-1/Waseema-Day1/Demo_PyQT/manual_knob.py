import sys
from PyQt5.QtWidgets import QApplication, QWidget,QSlider,QDial,QPushButton

app = QApplication(sys.argv)

window = QWidget()

s = QSlider(window)
s.move(300,50)

d = QDial(window)
d.move(50,50)

button = QPushButton(window, text = 'Change Value')
button.move(200,300)
def change_slider():
    s.setValue(50)

button.clicked.connect(change_slider)

s.valueChanged.connect(d.setValue)
d.valueChanged.connect(s.setValue)

window.show()
app.exec_()

