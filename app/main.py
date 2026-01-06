import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from ui.main_window import MainWindow
from ui.tray import SystemTray

dir = os.path.dirname(__file__)
path_icon = os.path.join(dir, "assets", "logo.svg")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_icon = QIcon(path_icon)
    app.setWindowIcon(app_icon)

    window = MainWindow()

    tray = SystemTray(app_icon)
    tray.show()

    def toggle_window():
        if window.isVisible():
            window.hide()
        else:
            window.show()
            window.activateWindow()

    tray.show_signal.connect(toggle_window)

    window.show()
    sys.exit(app.exec())