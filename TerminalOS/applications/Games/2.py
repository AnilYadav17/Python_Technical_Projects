import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont


class Demo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Utility Hub")
        self.resize(700, 550)

        title = QLabel("PyQt5 Demonstration")
        title.setFont(QFont("Arial", 18))
        title.setAlignment(Qt.AlignCenter)

        self.name = QLineEdit()
        self.name.setPlaceholderText("Enter your name")

        self.combo = QComboBox()
        self.combo.addItems([
            "Python",
            "Java",
            "C++",
            "JavaScript"
        ])

        self.checkbox = QCheckBox("I love Programming")

        self.radio1 = QRadioButton("Student")
        self.radio2 = QRadioButton("Teacher")

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        self.progress = QProgressBar()
        self.slider.valueChanged.connect(self.progress.setValue)

        self.lcd = QLCDNumber()
        self.slider.valueChanged.connect(self.lcd.display)

        self.timerLabel = QLabel("Clock")
        self.timerLabel.setAlignment(Qt.AlignCenter)
        self.timerLabel.setFont(QFont("Arial", 14))

        timer = QTimer(self)
        timer.timeout.connect(self.updateTime)
        timer.start(1000)

        self.output = QTextEdit()
        self.output.setReadOnly(True)

        btnInfo = QPushButton("Show Information")
        btnClear = QPushButton("Clear")
        btnExit = QPushButton("Exit")

        btnInfo.clicked.connect(self.showInfo)
        btnClear.clicked.connect(self.clearData)
        btnExit.clicked.connect(self.close)

        layout = QVBoxLayout()

        layout.addWidget(title)
        layout.addWidget(self.timerLabel)
        layout.addWidget(self.name)
        layout.addWidget(self.combo)
        layout.addWidget(self.checkbox)

        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)

        layout.addWidget(QLabel("Slider"))
        layout.addWidget(self.slider)

        layout.addWidget(self.progress)
        layout.addWidget(self.lcd)

        layout.addWidget(btnInfo)
        layout.addWidget(btnClear)
        layout.addWidget(btnExit)

        layout.addWidget(self.output)

        self.setLayout(layout)

    def updateTime(self):
        from PyQt5.QtCore import QTime
        self.timerLabel.setText(QTime.currentTime().toString())

    def showInfo(self):

        role = "None"

        if self.radio1.isChecked():
            role = "Student"

        elif self.radio2.isChecked():
            role = "Teacher"

        text = f"""
Name : {self.name.text()}

Favourite Language : {self.combo.currentText()}

Programming : {"Yes" if self.checkbox.isChecked() else "No"}

Role : {role}

Slider Value : {self.slider.value()}
"""

        self.output.setText(text)

        QMessageBox.information(
            self,
            "Information",
            "Data Submitted Successfully!"
        )

    def clearData(self):
        self.name.clear()
        self.output.clear()
        self.checkbox.setChecked(False)
        self.radio1.setChecked(False)
        self.radio2.setChecked(False)
        self.slider.setValue(0)


app = QApplication(sys.argv)

window = Demo()
window.show()

sys.exit(app.exec_())
