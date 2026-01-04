from PySide6.QtWidgets import QSystemTrayIcon, QApplication, QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import Signal

class SystemTray(QSystemTrayIcon):
    show_signal = Signal()
    close_signal = Signal()
    def __init__(self, icon, parent=None):
        super().__init__(icon = icon, parent=parent)

        tray_menu = QMenu()

        show_action = QAction("Open Arci", self)
        show_action.triggered.connect(self.show_signal.emit)

        quit_action = QAction("Exit", self)
        quit_action.triggered.connect(QApplication.instance().quit)

        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)

        self.setContextMenu(tray_menu)

        self.activated.connect(self.on_tray_icon_activated)

    def on_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger or reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self.show_signal.emit()