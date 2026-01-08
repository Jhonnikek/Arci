from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from core.commands import change_power_profile
from core.utils import get_energy_mode

class WidgetPowerProfile(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        power_profile_layout = QHBoxLayout()

        self.power_profile_label = QLabel("Mode ")
        layout.addWidget(self.power_profile_label)

        self.quiet_btn = QPushButton("Quiet")
        self.quiet_btn.clicked.connect(self.set_power_profile)
        power_profile_layout.addWidget(self.quiet_btn)

        self.balanced_btn = QPushButton("Balanced")
        self.balanced_btn.clicked.connect(self.set_power_profile)
        power_profile_layout.addWidget(self.balanced_btn)

        self.performance_btn = QPushButton("Performance")
        self.performance_btn.clicked.connect(self.set_power_profile)
        power_profile_layout.addWidget(self.performance_btn)

        layout.addLayout(power_profile_layout)
        self.setLayout(layout)
        self.power_profile_label.setText(f"Mode: {get_energy_mode()}")

    def set_power_profile(self):
        profile_btn = self.sender()
        profile = profile_btn.text()
        change_power_profile(profile)
        self.power_profile_label.setText(f"Mode: {profile}")