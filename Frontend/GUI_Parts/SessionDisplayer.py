from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QFrame
from PySide6.QtCore import Slot, Qt

from GUI_Parts import DataManager
from GameSignUpInfo import GameSignUpInfo

class TitleLabel(QLabel):
    """Class to represent a title label"""
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("background-color: lightgrey")

class SessionDisplayer(QWidget):
    """Displays details of the currently selected session"""

    # Maximum number of players the app will handle
    max_players = 8

    def __init__(self, data_manager: DataManager):
        super().__init__()

        self.data_manager = data_manager
        self.data_manager.selectedSessionChanged.connect(self.update_session)

        # Main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Layout part containing basic session info
        info_layout = QHBoxLayout()
        info_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        info_title_layout = QVBoxLayout()
        info_value_layout = QVBoxLayout()
        info_layout.addLayout(info_title_layout)
        info_layout.addSpacing(20)
        info_layout.addLayout(info_value_layout)
        main_layout.addLayout(info_layout)

        info_title_layout.addWidget(TitleLabel("Abenteuer"))
        self.adventure_name_value = QLabel("")
        info_value_layout.addWidget(self.adventure_name_value)

        info_title_layout.addWidget(TitleLabel("Spielleitung"))
        self.story_teller_value = QLabel("")
        info_value_layout.addWidget(self.story_teller_value)

        info_title_layout.addWidget(TitleLabel("System"))
        self.system_value = QLabel("")
        info_value_layout.addWidget(self.system_value)

        info_title_layout.addWidget(TitleLabel("Setting / Genre"))
        self.setting_value = QLabel("")
        info_value_layout.addWidget(self.setting_value)

        info_title_layout.addWidget(TitleLabel("Raum / Tisch"))
        self.place_value = QLabel("")
        info_value_layout.addWidget(self.place_value)

        info_title_layout.addWidget(TitleLabel("Tag / Uhrzeit"))
        self.time_value = QLabel("")
        info_value_layout.addWidget(self.time_value)

        info_title_layout.addWidget(TitleLabel("Hinweise und Warnungen"))
        self.trigger_warning_value = QLabel("")
        info_value_layout.addWidget(self.trigger_warning_value)

        main_layout.addSpacing(20)
        main_layout.addLayout(info_layout)

        # Layout part for adventure description
        main_layout.addWidget(TitleLabel("Beschreibung"))
        self.description_value = QLabel("")
        self.description_value.setWordWrap(True)
        main_layout.addWidget(self.description_value)

        # Main layout for all players
        main_layout.addSpacing(30)
        main_layout.addWidget(TitleLabel("Spieler"))
        player_main_layout = QHBoxLayout()
        main_layout.addLayout(player_main_layout)

        # Stores player layouts to en- and disable visibility
        self.player_layouts = []

        # Stores player text to update values
        self.player_values = []

        #Layout for players 1-4
        player_first_layout = QVBoxLayout()

        player_first_layout.addWidget(self.create_player_layout("1"))
        player_first_layout.addWidget(self.create_player_layout("2"))
        player_first_layout.addWidget(self.create_player_layout("3"))
        player_first_layout.addWidget(self.create_player_layout("4"))
        player_first_layout.addStretch()

        # Layout for players 5-8
        player_second_layout = QVBoxLayout()

        player_second_layout.addWidget(self.create_player_layout("5"))
        player_second_layout.addWidget(self.create_player_layout("6"))
        player_second_layout.addWidget(self.create_player_layout("7"))
        player_second_layout.addWidget(self.create_player_layout("8"))
        player_second_layout.addStretch()

        player_main_layout.addLayout(player_first_layout)
        player_main_layout.addLayout(player_second_layout)
        player_main_layout.addStretch()

    def create_player_layout(self, player_label):
        """Creates player layout and adds respective values to player lists"""

        player_layout = QHBoxLayout()
        player_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        player_layout.addWidget(TitleLabel(player_label))
        player_layout.addSpacing(0)
        player_value = QLabel("")
        player_layout.addWidget(player_value)

        # Frame is used to enable and disable player slot as needed
        frame = QFrame()
        frame.setLayout(player_layout)

        self.player_values.append(player_value)
        self.player_layouts.append(frame)

        return frame


    @Slot(GameSignUpInfo)
    def update_session(self, session : GameSignUpInfo):
        """Updates session info"""

        self.adventure_name_value.setText(session.gameName)
        self.story_teller_value.setText(session.storyTeller)
        self.system_value.setText(session.systemName)
        self.setting_value.setText(session.settingName)
        self.place_value.setText(session.place)
        self.time_value.setText(session.time)
        self.description_value.setText(session.description)
        self.trigger_warning_value.setText(session.triggers)

        #Fill and en-/disable player slots as needed
        for i in range(session.maxPlayers):
            if len(session.players) > i:
                self.player_values[i].setText(session.players[i])
            else:
                self.player_values[i].setText("")
            self.player_layouts[i].show()

        for i in range(session.maxPlayers, self.max_players):
            self.player_values[i].setText("")
            self.player_layouts[i].hide()