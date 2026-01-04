from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from ui.components.power_profile import WidgetPowerProfile
from ui.components.keyboard import WidgetKeyboard
from ui.components.bettery import WidgetBattery

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Arci")
        self.setFixedSize(300, 275)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()

        self.power_profiles = WidgetPowerProfile()
        main_layout.addWidget(self.power_profiles)

        self.keyboard = WidgetKeyboard()
        main_layout.addWidget(self.keyboard)

        self.battery = WidgetBattery()
        main_layout.addWidget(self.battery)

        main_layout.addStretch()
        self.setLayout(main_layout)
        central_widget.setLayout(main_layout)