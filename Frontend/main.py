import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Slot
from GUI_Parts import SessionDisplayer
from GUI_Parts.AboutWindow import AboutWindow
from GUI_Parts.DataManager import DataManager
from GUI_Parts.SessionSelectorList import SessionSelectorList
from GUI_Parts.ToolWindowBar import ToolWindowBar
from GUI_Parts.SessionDisplayer import SessionDisplayer

# Main window of RundenaushangApp
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rabenaushang")

        # Main class managing data flow through app
        self.data_manager = DataManager()

        # Main menu
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)

        about_action = menubar.addAction("About")
        about_action.triggered.connect(self.show_about)

        #layout
        main_widget = QWidget()
        layout = QVBoxLayout(main_widget)

        tool_bar = ToolWindowBar(self.data_manager)

        layout.addWidget(tool_bar)

        sublayout = QHBoxLayout()

        session_selector = SessionSelectorList(self.data_manager)
        sublayout.addWidget(session_selector)

        session_displayer = SessionDisplayer(self.data_manager)
        sublayout.addWidget(session_displayer)

        layout.addLayout(sublayout)

        self.setCentralWidget(main_widget)

        # About popup window
        self.about_window = AboutWindow()

    def show_about(self):
        self.about_window.show()

    def closeEvent(self, event):
        self.about_window.destroy()
        event.accept()  # let the window close

# Create and start application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()