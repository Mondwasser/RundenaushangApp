class GameSignUpInfo(object):
    """Holds all information of a game session sign-in sheet"""

    def __init__(self, game_name, story_teller, system_name, setting_name, place, time, description, players, triggers, tags, recomended_age, max_players):
        self.gameName = game_name
        self.storyTeller = story_teller
        self.systemName = system_name
        self.settingName = setting_name
        self.place = place
        self.time = time
        self.description = description
        self.players = players
        self.triggers = triggers
        self.tags = tags
        self.recommendedAge = recomended_age
        self.maxPlayers = max_players