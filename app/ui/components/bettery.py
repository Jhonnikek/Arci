from PySide6.QtWidgets import QWidget, QVBoxLayout, QSlider, QLabel
from PySide6.QtCore import Qt

class WidgetBattery(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.battery_label = QLabel("Battery Charge Limit")
        layout.addWidget(self.battery_label)
        
        self.battery_slider = QSlider(Qt.Horizontal)
        self.battery_slider.setMinimum(0)
        self.battery_slider.setMaximum(100)
        layout.addWidget(self.battery_slider)

        self.setLayout(layout)