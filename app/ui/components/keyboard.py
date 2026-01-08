from core.commands import change_aura_mode, change_color, change_rgb_lvl
from PySide6.QtCore import QSettings, Qt
from PySide6.QtWidgets import QColorDialog,QComboBox, QHBoxLayout, QLabel, QPushButton, QSlider, QVBoxLayout, QWidget
from core.utils import get_keyboard_brightness

class WidgetKeyboard(QWidget):
    def __init__(self):
        super().__init__()

        self.color = ""
        layout = QVBoxLayout()
        keyboard_layout = QHBoxLayout()

        self.keyboard_label = QLabel("Keyboard Backlight")
        layout.addWidget(self.keyboard_label)

        self.aura_mode_combobox = QComboBox()
        self.aura_mode_combobox.addItems(
            ["Static", "Breathe", "Rainbow-Cycle", "Pulse"]
        )
        self.aura_mode_combobox.currentTextChanged.connect(self.set_aura_mode)
        keyboard_layout.addWidget(self.aura_mode_combobox)

        self.rgb_levels = ["off", "low", "med", "high"]
        self.rgb_levels_slider = QSlider(Qt.Horizontal)
        self.rgb_levels_slider.setMinimum(0)
        self.rgb_levels_slider.setMaximum(3)
        self.rgb_levels_slider.sliderReleased.connect(self.set_rgb_level)
        self.rgb_levels_slider.valueChanged.connect(self.update_label)
        keyboard_layout.addWidget(self.rgb_levels_slider)

        self.color_btn = QPushButton(" ")
        self.color_btn.clicked.connect(self.pick_color)
        self.color_btn.setFixedSize(40, 40)
        keyboard_layout.addWidget(self.color_btn)

        layout.addLayout(keyboard_layout)
        self.setLayout(layout)
        self.load_settings()

        brightness = get_keyboard_brightness()
        self.rgb_levels_slider.setValue(int(brightness))
        self.update_label(int(brightness))

    def save_settings(self):
        settings = QSettings()
        settings.setValue("aura_mode", self.aura_mode_combobox.currentText())
        settings.setValue("color", self.color)

    def load_settings(self):
        settings = QSettings()
        aura_mode = settings.value("aura_mode", "")
        color = settings.value("color", "")

        self.aura_mode_combobox.setCurrentText(aura_mode)
        self.color = color
        btn_color = f"QPushButton {{ color: {color};}}"
        self.color_btn.setStyleSheet(btn_color)

    def update_label(self, value):
        levels = {0: "Off", 1: "Low", 2: "Medium", 3: "High"}
        self.keyboard_label.setText(f"Keyboard Backlight: {levels.get(value)}")

    def pick_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            color_name = color.name()
            self.color = color_name
            btn_color = f"QPushButton {{ color: {color_name};}}"
            self.color_btn.setStyleSheet(btn_color)
            self.set_color(color_name)
            self.save_settings()

    def set_color(self, color_name):
        mode = self.aura_mode_combobox.currentText()
        color_name = color_name.lstrip("#")
        self.color = color_name
        change_color(mode.lower(), color_name)
        self.set_rgb_level()

    def set_aura_mode(self):
        mode = self.aura_mode_combobox.currentText()
        change_aura_mode(mode.lower())

        if mode != "Rainbow-Cycle":
            color = self.color
            change_color(mode.lower(), color)
        
        self.save_settings()

    def set_rgb_level(self):
        value = self.rgb_levels_slider.value()
        level = self.rgb_levels[value]
        change_rgb_lvl(level)
