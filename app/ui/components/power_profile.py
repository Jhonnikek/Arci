from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from core.commands import change_profile

class WidgetPowerProfile(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        power_profile_layout = QHBoxLayout()

        self.power_profile_label = QLabel("Mode: ")
        layout.addWidget(self.power_profile_label)

        self.btn_low_power = QPushButton("Low Power")
        self.btn_low_power.clicked.connect(self.power_profile)
        power_profile_layout.addWidget(self.btn_low_power)

        self.btn_balanced = QPushButton("Balanced")
        self.btn_balanced.clicked.connect(self.power_profile)
        power_profile_layout.addWidget(self.btn_balanced)

        self.btn_performance = QPushButton("Performance")
        self.btn_performance.clicked.connect(self.power_profile)
        power_profile_layout.addWidget(self.btn_performance)

        layout.addLayout(power_profile_layout)
        self.setLayout(layout)

    def power_profile(self):
        btn = self.sender()
        profile = btn.text()
        change_profile(profile)
        self.power_profile_label.setText(f"Mode: {profile}")