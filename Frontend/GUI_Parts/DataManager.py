from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget

from GameSignUpInfo import GameSignUpInfo

# IMPORTANT needs to import all available writers
from Writer import SessionSheetWriterBase, RabenthingPdfWriter


class DataManager(QWidget):
    """Handles data and data flow through the GUI"""

    sessionsUpdated = Signal(list)
    """Is triggered when the list of sessions is changed"""

    selectedSessionChanged = Signal(GameSignUpInfo)
    """Is triggered when another session is selected"""

    def __init__(self):
        super().__init__()

        # Create a list with all available writers
        self.writers = {}
        """All writers that are capable of processing GameSignUpInfo objects into external files"""
        for writer in SessionSheetWriterBase.SessionSheetWriterBase.__subclasses__():
            self.writers[writer.name] = writer

        self.sessions = []
        """Currently loaded sessions"""

        self.has_sessions = False
        """Whether there are sessions loaded"""

    def set_sessions(self, sessions : list[GameSignUpInfo]):
        """Change currently loaded sessions"""

        self.sessions.clear()

        for item in sessions:
            if isinstance(item,GameSignUpInfo):
                self.sessions.append(item)

        if len(self.sessions)>0:
            self.has_sessions = True

        self.sessionsUpdated.emit(sessions)

    @Slot(int)
    def update_selected_session(self, session_id : int):
        """Updates the currently selected session"""
        if len(self.sessions) > session_id:
            self.selectedSessionChanged.emit(self.sessions[session_id])