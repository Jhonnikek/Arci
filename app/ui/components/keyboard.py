from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton,QSlider,QComboBox

from PySide6.QtCore import Qt

class WidgetKeyboard(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        self.aura = QComboBox()
        self.aura.addItems(["Static", "Breathe", "Cycle", "Wave", "Pulse"])

        self.aura_levels = ["off", "low", "med", "high"]
        self.aura_slider = QSlider(Qt.Horizontal)
        self.aura_slider.setMinimum(0)
        self.aura_slider.setMaximum(3)

        self.aura_color = QPushButton(" ")
        self.aura_color.setFixedSize(40, 40)

        layout = QHBoxLayout()
        layout.addWidget(self.aura)
        layout.addWidget(self.aura_slider)
        layout.addWidget(self.aura_color)

        self.setLayout(layout)
