from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QSlider, QComboBox,QColorDialog, QLabel

from PySide6.QtCore import Qt
from core.commands import change_color

class WidgetKeyboard(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        keyboard_layout = QHBoxLayout()

        self.keyboard_label = QLabel("Keyboard")
        layout.addWidget(self.keyboard_label)

        self.keyboard = QComboBox()
        self.keyboard.addItems(["Static", "Breathe", "rainbow-Cycle", "rainbow-Wave", "Pulse"])
        keyboard_layout.addWidget(self.keyboard)

        self.keyboard_levels = ["off", "low", "med", "high"]
        self.keyboard_slider = QSlider(Qt.Horizontal)
        self.keyboard_slider.setMinimum(0)
        self.keyboard_slider.setMaximum(3)
        keyboard_layout.addWidget(self.keyboard_slider)

        self.keyboard_color = QPushButton(" ")
        self.keyboard_color.clicked.connect(self.show_color_dialog)
        self.keyboard_color.setFixedSize(40, 40)
        keyboard_layout.addWidget(self.keyboard_color)

        layout.addLayout(keyboard_layout)
        self.setLayout(layout)

    def show_color_dialog(self):
        color = QColorDialog.getColor()
        mode = self.keyboard.currentText()
        if color.isValid():
            color_name = color.name()
            color_name = color_name.lstrip("#")
            change_color(mode.lower(), color_name)