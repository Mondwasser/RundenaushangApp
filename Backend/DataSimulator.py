from abc import abstractmethod

from GameSignUpInfo import GameSignUpInfo
from Writer.SessionSheetWriterBase import SessionSheetWriterBase


class DataSimulator(object):
    """Holds test data of game sessions"""

    #All is well
    all_is_well = GameSignUpInfo("Das Leiden, das Eschweiler befiel",
                            "Dennis // Steini // Mondwasser",
                            "Daggerheart",
                            "Unheimliche Fantasy, Horror",
                            "Fenrir",
                            "Freitag Abendthing",
                            "Eine kleine Abenteurergruppe hat das Lager für die Nacht aufgeschlagen. Das Essen röstet über dem Lagerfeuer, als sich eine einsame Reisende zu der Gruppe gesellt.\nIm Tausch für einen Teil des Mahls und einem warmen Platz am Feuer, bietet sie eine Geschichte an. Begierig, die Langeweile des Abends zu vertreiben, nimmt die Gruppe das Angebot an. \nUnd so beginnt die Fremde ihre Erzählung von jenem Leid, das dereinst Eschweiler befiel. \n \nCharaktere werden gestellt, Systemkenntnis nicht nötig, Ab 18 Jahren",
                            ["Player1", "Player2", "Player3", "Player4", "Player5"],
                           "Gewalt, Tod, Suicid",
                           None, None,
                           5
                            )
    """Session without expected problems"""
    too_many_players = GameSignUpInfo("Das Leiden, das Eschweiler befiel",
                           "Dennis // Steini // Mondwasser",
                           "Daggerheart",
                           "Unheimliche Fantasy, Horror",
                           "Fenrir",
                           "Freitag Abendthing",
                           "Eine kleine Abenteurergruppe hat das Lager für die Nacht aufgeschlagen. Das Essen röstet über dem Lagerfeuer, als sich eine einsame Reisende zu der Gruppe gesellt.\nIm Tausch für einen Teil des Mahls und einem warmen Platz am Feuer, bietet sie eine Geschichte an. Begierig, die Langeweile des Abends zu vertreiben, nimmt die Gruppe das Angebot an. \nUnd so beginnt die Fremde ihre Erzählung von jenem Leid, das dereinst Eschweiler befiel. \n \nCharaktere werden gestellt, Systemkenntnis nicht nötig, Ab 18 Jahren",
                           ["Player1", "Player2", "Player3", "Player4", "Player5", "Player6"],
                           "Gewalt, Tod, Suicid",
                           None, None,
                           5
                           )
    """Session containing more players than player slots"""
    no_adventure_name = GameSignUpInfo(None,
                                 "Dennis // Steini // Mondwasser",
                                 "Daggerheart",
                                 "Unheimliche Fantasy, Horror",
                                 "Fenrir",
                                 "Freitag Abendthing",
                                 "Eine kleine Abenteurergruppe hat das Lager für die Nacht aufgeschlagen. Das Essen röstet über dem Lagerfeuer, als sich eine einsame Reisende zu der Gruppe gesellt.\nIm Tausch für einen Teil des Mahls und einem warmen Platz am Feuer, bietet sie eine Geschichte an. Begierig, die Langeweile des Abends zu vertreiben, nimmt die Gruppe das Angebot an. \nUnd so beginnt die Fremde ihre Erzählung von jenem Leid, das dereinst Eschweiler befiel. \n \nCharaktere werden gestellt, Systemkenntnis nicht nötig, Ab 18 Jahren",
                                 ["Player1", "Player2", "Player3", "Player4", "Player5"],
                                 "Gewalt, Tod, Suicid",
                                 None, None,
                                 5
                                 )
    """Session lacking a session name"""
    empty_adventure_name = GameSignUpInfo("",
                                       "Dennis // Steini // Mondwasser",
                                       "Daggerheart",
                                       "Unheimliche Fantasy, Horror",
                                       "Fenrir",
                                       "Freitag Abendthing",
                                       "Eine kleine Abenteurergruppe hat das Lager für die Nacht aufgeschlagen. Das Essen röstet über dem Lagerfeuer, als sich eine einsame Reisende zu der Gruppe gesellt.\nIm Tausch für einen Teil des Mahls und einem warmen Platz am Feuer, bietet sie eine Geschichte an. Begierig, die Langeweile des Abends zu vertreiben, nimmt die Gruppe das Angebot an. \nUnd so beginnt die Fremde ihre Erzählung von jenem Leid, das dereinst Eschweiler befiel. \n \nCharaktere werden gestellt, Systemkenntnis nicht nötig, Ab 18 Jahren",
                                       ["Player1", "Player2", "Player3", "Player4", "Player5"],
                                       "Gewalt, Tod, Suicid",
                                       None, None,
                                       5
                                       )
    """Session with an empty adventure name"""
    list_all_is_well = [
        GameSignUpInfo("Das Leiden, das Eschweiler befiel",
                       "Dennis // Steini // Mondwasser",
                       "Daggerheart",
                       "Unheimliche Fantasy, Horror",
                       "Fenrir",
                       "Freitag Abendthing",
                       "Eine kleine Abenteurergruppe hat das Lager für die Nacht aufgeschlagen. Das Essen röstet über dem Lagerfeuer, als sich eine einsame Reisende zu der Gruppe gesellt.\nIm Tausch für einen Teil des Mahls und einem warmen Platz am Feuer, bietet sie eine Geschichte an. Begierig, die Langeweile des Abends zu vertreiben, nimmt die Gruppe das Angebot an. \nUnd so beginnt die Fremde ihre Erzählung von jenem Leid, das dereinst Eschweiler befiel. \n \nCharaktere werden gestellt, Systemkenntnis nicht nötig, Ab 18 Jahren",
                       ["Player1", "Player2", "Player3", "Player4", "Player5"],
                       "Gewalt, Tod, Suicid",
                       None, None,
                       8
                       ),
        GameSignUpInfo("Das Grauen aus der Tiefe",
                       "Dennis // Steini // Mondwasser",
                       "Wrath and Glory",
                       "Warhammer 40k, Horror",
                       "Fenrir",
                       "Freitag Morgenthing",
                       "In den Archiven von Cinis Sperum wurden Hinweise auf den Verbleib einer uralten Reliquie gefunden. Bischof Severian Holt schickt eine kleine Gruppe seiner engsten Vertrauten los die Reliquie zu bergen, bevor einer seiner Rivalen etwas davon mitbekommt und ihm den Fund streitig machen kann. \n\nWissen über das System wird nicht benötigt (Es wird sowieso fast nicht genutzt in dem Abenteuer).Einsteiger und Veteranen willkommen.Das Abenteuer ist ein Horrorabenteuer für Spieler ab 18 Jahren. Fokus ist Atmosphäre und Horror. ",
                       ["Player1", "Player2", "Player3", "Player4", "Player5"],
                       "Gewalt, Body-Horror, Krankheit, Wahnsinn",
                       None, None,
                       5
                       ),
        GameSignUpInfo("Ulmenholz - Lyssandras erster Tag",
                       "Dennis // Steini // Mondwasser",
                       "Daggerheart",
                       "Gemütliche Fantasy",
                       "Sleipnir",
                       "Donnerstag Abendthing",
                       "Ihr seid alle jugendliche Delinquenten, verurteilt zu einer perfiden Art des Zivildienstes: Ihr müsst für Jahr und Tag als Miliz in dem langweiligsten Dorf des Landes dienen, in Ulmenholz. Eine beinahe Schlägerei war das spannendste, das hier in den letzten zwei Wochen passiert ist. Leider haben sich die beiden vertragen, bevor es wirklich interessant werden konnte. Eine Einladung von Lyssandra zu einem Abendessen im Magierturm, ist da ein Angebot, das einfach nicht auszuschlagen ist! Charaktere werden gestellt, \n\n Systemwissen nicht notwendig",
                       ["Player1", "Player2"],
                       "",
                       None, None,
                       3
                       )
    ]
    """List with three valid sessions"""
