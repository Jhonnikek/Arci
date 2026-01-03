from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from ui.components.power_profile import WidgetPowerProfile
from ui.components.gpu_mode import WidgetGpuMode

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Arci")
        self.setFixedSize(300, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()

        self.power_profile_label = QLabel("Mode: ")
        main_layout.addWidget(self.power_profile_label)
        self.power_profiles = WidgetPowerProfile()
        main_layout.addWidget(self.power_profiles)

        self.gpu_mode_label = QLabel("GPU Mode")
        main_layout.addWidget(self.gpu_mode_label)
        self.gpu_mode = WidgetGpuMode()
        main_layout.addWidget(self.gpu_mode)

        main_layout.addStretch()
        self.setLayout(main_layout)
        central_widget.setLayout(main_layout)

    """def power_profile(self):
        btn = self.sender()
        level = btn.text()
        change_profile(level)
        self.power_profile_label.setText(f"Mode: {level}")"""
