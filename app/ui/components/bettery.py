from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSlider, QComboBox
from PySide6.QtCore import Qt

class WidgetBattery(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        self.battery_slider = QSlider(Qt.Horizontal)
        self.battery_slider.setMinimum(0)
        self.battery_slider.setMaximum(100)

        layout = QHBoxLayout()
        layout.addWidget(self.battery_slider)

        self.setLayout(layout)

