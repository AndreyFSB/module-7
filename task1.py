from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt


app = QApplication([])
label = QLabel('Hello World!')

font = label.font()
font.setPointSize(24)
label.setFont(font)

label.setAlignment(Qt.AlignmentFlag.AlignRight)
label.show()
app.exec()