from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QSlider, QComboBox,QColorDialog, QLabel

from PySide6.QtCore import Qt
from core.commands import change_color, change_aura_mode, change_rgb_lvl

class WidgetKeyboard(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        keyboard_layout = QHBoxLayout()

        self.keyboard_label = QLabel("Keyboard")
        layout.addWidget(self.keyboard_label)

        self.aura_mode_combobox = QComboBox()
        self.aura_mode_combobox.addItems(["Static", "Breathe", "Rainbow-Cycle", "Pulse"])
        self.aura_mode_combobox.currentTextChanged.connect(self.set_aura_mode)
        keyboard_layout.addWidget(self.aura_mode_combobox)

        self.rgb_levels = ["off", "low", "med", "high"]
        self.rgb_levels_slider = QSlider(Qt.Horizontal)
        self.rgb_levels_slider.setMinimum(0)
        self.rgb_levels_slider.setMaximum(3)
        self.rgb_levels_slider.sliderReleased.connect(self.on_rgb_level_changed)
        keyboard_layout.addWidget(self.rgb_levels_slider)

        self.color_btn = QPushButton(" ")
        self.color_btn.clicked.connect(self.pick_color)
        self.color_btn.setFixedSize(40, 40)
        keyboard_layout.addWidget(self.color_btn)

        layout.addLayout(keyboard_layout)
        self.setLayout(layout)

    def pick_color(self):
        color = QColorDialog.getColor()
        mode = self.aura_mode_combobox.currentText()
        if color.isValid():
            color_name = color.name()
            btn_color = f"QPushButton {{ color: {color_name};}}"
            self.color_btn.setStyleSheet(btn_color)
            color_name = color_name.lstrip("#")
            change_color(mode.lower(), color_name)

    def set_aura_mode(self):
        mode = self.aura_mode_combobox.currentText()
        change_aura_mode(mode.lower())

    def on_rgb_level_changed(self):
        value = self.rgb_levels_slider.value()
        level = self.rgb_levels[value]
        change_rgb_lvl(level)