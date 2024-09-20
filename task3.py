from PyQt5.QtWidgets import *

app = QApplication([])
widget = QWidget()
layout = QVBoxLayout()
button = QPushButton('Click')
checkable_button = QPushButton()
checkable_button.setCheckable(True)
clicked_count = 0
count_button = QPushButton(f'Click count = {clicked_count}')
label = QLabel('Checked')

layout.addWidget(button)
layout.addWidget(checkable_button)
layout.addWidget(count_button)
layout.addWidget(label)

widget.setLayout(layout)

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec()

def checkable_button_toggled(checked: bool):
    checkable_button.setText('Включено' if checked else 'Выключено')
    label.setVisible(checked)

def on_count_button_clicked():
    global clicked_count
    clicked_count += 1
    count_button.setText(f'Click count = {clicked_count}')

checkable_button_toggled(False)

button.clicked.connect(on_button_clicked)
checkable_button.toggled.connect(checkable_button_toggled)
count_button.clicked.connect(on_count_button_clicked)
widget.show()
app.exec()