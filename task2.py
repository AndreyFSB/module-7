from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
layout = QFormLayout()
layout.addRow('Top', QPushButton('Top'))
layout.addRow('Bottom', QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec()