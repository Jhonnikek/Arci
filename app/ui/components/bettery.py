from PySide6.QtWidgets import QWidget, QVBoxLayout, QSlider, QLabel
from PySide6.QtCore import Qt
from core.commands import change_battery_limit
from core.utils import get_battery_limit

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
        self.battery_slider.valueChanged.connect(self.update_label)
        self.battery_slider.sliderReleased.connect(self.set_battery_charge_limit)

        self.setLayout(layout)
        limit = get_battery_limit()
        self.battery_slider.setValue(int(limit))
        self.update_label(limit)

    def update_label(self, limit):
        self.battery_label.setText(f"Battery Charge Limit: {limit}%")

    def set_battery_charge_limit(self):
        limit = self.battery_slider.value()
        change_battery_limit(str(limit))