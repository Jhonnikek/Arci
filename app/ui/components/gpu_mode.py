from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton

class WidgetGpuMode(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        self.btn_integrated = QPushButton("Intregrated")

        self.btn_hybrid = QPushButton("Hybrid")

        self.btn_dedicated = QPushButton("dedicated")

        layout.addWidget(self.btn_integrated)
        layout.addWidget(self.btn_hybrid)
        layout.addWidget(self.btn_dedicated)

        self.setLayout(layout)