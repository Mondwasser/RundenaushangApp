import os
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from GameSignUpInfo import GameSignUpInfo
from Writer.SessionSheetWriterBase import SessionSheetWriterBase

gamesignupinfo_to_pdftemplate_map = {
        "gameName": "Abenteuer",
        "storyTeller": "SL",
        "systemName": "System",
        "settingName": "Setting",
        "place": "Tisch",
        "time": "Zeit",
        "description": "Beschreibung",
        "players": ["Spieler 1", "Spieler 2", "Spieler 3", "Spieler 4", "Spieler 5", "Spieler 6", "Spieler 7", "Spieler 8"],
        "triggers": "Trigger",
        "tags": None,
        "recommendedAge": None
    }
"""Contains the information to map GameSignUpInfo attributes to fields in the template"""

class RabenthingPdfWriter(SessionSheetWriterBase):
    """Writer to generate session printouts for Rabenthing"""

    name = "RabenthingPdfWriter"
    """Name of the writer"""

    # Check these if template changes
    max_players_sheet = 8
    """Maximum allowed number of players in the template"""

    players_key = "players"
    """Key in map that holds player information"""

    blocked_player_signifier = "-----------------------------------------"
    """This will be inserted into the player field when the slot is not available"""

    def write(self, session: GameSignUpInfo, target_folder : str) -> None:
        """Writes session info to file"""

        # Currently only can handle GameSignUpInfo type objects
        if not(isinstance(session, GameSignUpInfo)):
            raise Exception("session must be of type GameSignUpInfo")

        # read the PDF document
        reader = PdfReader("D:/Projekte/Programmieren/RundenaushangsApp/Backend/Writer/Templates/RabenthingTemplate.pdf")
        # extract its text fields
        fields = reader.get_form_text_fields()

        #Create dictionary with values to be put into form
        new_fields = {}
        info_attributes = [a for a in dir(session) if not a.startswith("__")]

        for attribute in info_attributes:
            attribute_value = getattr(session, attribute)
            if attribute_value is None:
                continue
            if isinstance(attribute_value, str):
                if (attribute in gamesignupinfo_to_pdftemplate_map and
                    gamesignupinfo_to_pdftemplate_map[attribute] is not None):
                    new_key = str(gamesignupinfo_to_pdftemplate_map[attribute])
                    new_fields.update({new_key: getattr(session, attribute)})
            elif isinstance(attribute_value, list):
                if attribute in gamesignupinfo_to_pdftemplate_map:
                    transfer_list = gamesignupinfo_to_pdftemplate_map[attribute]
                    if transfer_list is not None and transfer_list is list:
                        value_dict = getattr(session, attribute)
                        max_length = min(len(transfer_list), len(value_dict))
                        for i in range(max_length):
                            new_key = transfer_list[i]
                            new_fields.update({new_key: value_dict[i]})
            else:
                pass

        #Block unavailable slots
        value_dict = gamesignupinfo_to_pdftemplate_map[self.players_key]
        for i in range (session.maxPlayers, self.max_players_sheet):
            new_key = value_dict[i]
            new_fields.update({new_key : self.blocked_player_signifier})

        # Open template
        writer = PdfWriter()
        writer.append(reader)

        # Fill in fields of template
        for page in writer.pages:
            writer.update_page_form_field_values(
                page,
                new_fields,
                auto_regenerate=False
            )

        target_folder = os.path.dirname(target_folder)

        if not os.path.isdir(target_folder):
            os.makedirs(target_folder)

        # Create file name from session name
        file_name = session.gameName

        if file_name is None or file_name == "":
            file_name = "Unbekanntes Abenteuer"

        output_filename = os.sep.join([target_folder, (file_name + ".pdf")])

        #Add 1s to the file name until name is unique
        while Path(output_filename).exists():
            file_name = file_name + "1"
            if len(file_name) > 50:
                raise Exception("Too many files with the same name " + file_name)
            output_filename = os.sep.join([target_folder, (file_name + ".pdf")])

        with open(output_filename, "wb") as fp:
            writer.write(fp)