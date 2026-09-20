from PySide6.QtWidgets import QAbstractItemView, QListWidget, QListWidgetItem
from PySide6.QtCore import Slot, Signal
from GUI_Parts import DataManager

class ListItemWithID(QListWidgetItem):
    """ListItem with ID"""
    def __init__(self, game_name : str, game_id: int):
        super().__init__(game_name)
        self.game_id = game_id

class SessionSelectorList(QListWidget):
    """Widget displaying a list of sessions"""

    selectedSessionChanged = Signal(int)
    """Signal emitted when a new session is selected"""

    def __init__(self, data_manager : DataManager.DataManager):
        super().__init__()

        self.data_manager = data_manager
        data_manager.sessionsUpdated.connect(self.update_sessions)

        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.itemSelectionChanged.connect(self.on_click)

        self.selectedSessionChanged.connect(data_manager.update_selected_session)

    @Slot(list)
    def update_sessions(self, sessions : list):
        """Update the list of sessions"""

        self.clear()

        i = 0
        for item in sessions:
                self.addItem(ListItemWithID(item.gameName, i))
                i += 1

    def on_click(self):
        """Emits selectedSessionChanged signal when a new session is selected"""
        self.selectedSessionChanged.emit(self.currentItem().game_id)

