from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Penalty Game")

label = QLabel("Shoot your shot!")

btn_left = QPushButton("Left")
btn_center = QPushButton("Center")
btn_right = QPushButton("Right")

def shoot_left():
    label.setText("You shot left!")

def shoot_center():
    label.setText("You shot center!")

def shoot_right():
    label.setText("You shot right!")

btn_left.clicked.connect(shoot_left)
btn_center.clicked.connect(shoot_center)
btn_right.clicked.connect(shoot_right)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(btn_left)
layout.addWidget(btn_center)
layout.addWidget(btn_right)

window.setLayout(layout)
window.show()

sys.exit(app.exec())



