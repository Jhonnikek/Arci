from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton

class WidgetPowerProfile(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        self.btn_low_power = QPushButton("Low Power")

        self.btn_balanced = QPushButton("Balanced")

        self.btn_performance = QPushButton("Performance")

        layout.addWidget(self.btn_low_power)
        layout.addWidget(self.btn_balanced)
        layout.addWidget(self.btn_performance)

        self.setLayout(layout)