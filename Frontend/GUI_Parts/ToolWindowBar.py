from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QComboBox
import DataSimulator
from PySide6.QtCore import Slot
from GUI_Parts import DataManager
from tkinter.filedialog import askdirectory

class ToolWindowBar(QWidget):
    """Widget for tools"""
    def __init__(self, data_manager : DataManager.DataManager):
        super().__init__()

        self.data_manager = data_manager

        get_data_button = QPushButton("Get Data")
        get_data_button.clicked.connect(self.get_data)

        self.create_pdfs_button = QPushButton("Create Pdfs")
        self.create_pdfs_button.clicked.connect(self.create_pdfs)
        self.create_pdfs_button.setEnabled(False)

        self.writer_box = QComboBox()

        for writer in data_manager.writers:
            self.writer_box.addItem(writer)

        layout = QHBoxLayout(self)
        layout.addWidget(get_data_button)
        layout.addWidget(self.writer_box)
        layout.addWidget(self.create_pdfs_button)

        data_manager.sessionsUpdated.connect(self.update_creator_visibility)

    def get_data(self):
        """Get session infos"""
        # TODO Dummy implementation that gets example data. To be replaced by mechanism to get real data
        self.data_manager.set_sessions(DataSimulator.DataSimulator().list_all_is_well)

    @Slot(list)
    def update_creator_visibility(self, sessions: list):
        """Updates the visibility of the PDF creator button"""
        self.create_pdfs_button.setEnabled(len(sessions) > 0)

    def create_pdfs(self):
        """Creates PDFs"""

        # Create writer of selected type
        writer_class = self.data_manager.writers[self.writer_box.currentText()]

        if writer_class is None:
            return

        writer= writer_class()

        target_folder = askdirectory(title='Select Folder')

        # Exit without bothering user with message
        if target_folder == '':
            return

        target_folder += '/'

        for session in self.data_manager.sessions:
            writer.write(session, target_folder)

        # TODO Create popup with success / failure / go to folder