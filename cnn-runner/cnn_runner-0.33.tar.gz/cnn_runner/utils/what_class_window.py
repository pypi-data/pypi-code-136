from PyQt5.QtWidgets import QLabel, QWidget, QGroupBox, QFormLayout, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt


class WhatClassWindow(QWidget):
    def __init__(self, parent, class_names=["aes", "forest", "water"]):
        super().__init__(parent)
        self.setWindowTitle("Выбор класса пикселей")
        self.setWindowFlag(Qt.Tool)

        self.class_names = class_names

        # Настройки обнаружения

        self.selected_class = "water"

        layout = QFormLayout()

        self.class_combo = QComboBox()

        self.class_combo.addItems(self.class_names)
        class_label = QLabel("Класс пикселей:")

        layout.addRow(class_label, self.class_combo)

        btnLayout = QHBoxLayout()

        self.okBtn = QPushButton('Принять', self)
        self.okBtn.clicked.connect(self.on_ok_clicked)

        self.cancelBtn = QPushButton('Отменить', self)
        self.cancelBtn.clicked.connect(self.on_cancel_clicked)

        btnLayout.addWidget(self.okBtn)
        btnLayout.addWidget(self.cancelBtn)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layout)
        mainLayout.addLayout(btnLayout)
        self.setLayout(mainLayout)

        self.resize(500, 150)

    def on_ok_clicked(self):
        self.selected_class = self.class_combo.currentText()
        print(self.selected_class)
        self.close()

    def on_cancel_clicked(self):
        self.close()
