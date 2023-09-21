from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QHBoxLayout,QVBoxLayout
# 

app = QApplication([])
window = QWidget()
window.resize(600,500)
window.setWindowTitle("Button App")

# Create all objects
btn1 = QPushButton("1")
btn2 = QPushButton("2")
btn3 = QPushButton("3")
btn4 = QPushButton("4")
btn5 = QPushButton("5")

#Create our design/layouts
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(btn1, alignment=Qt.AlignLeft)
row1.addWidget(btn2, alignment=Qt.AlignRight)

row2.addWidget(btn3, alignment=Qt.AlignCenter)

row3.addWidget(btn4, alignment=Qt.AlignLeft)
row3.addWidget(btn5, alignment=Qt.AlignRight)


master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

window.setLayout(master_layout)






window.show()
app.exec_()