from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QLabel


class AboutWindow(QMainWindow):
    """Popup window containing information about the app"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setFixedSize(QSize(400, 300))

        content = QLabel("Diese App wurde entwickelt von Dennis Steinfeld")
        content.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(content)