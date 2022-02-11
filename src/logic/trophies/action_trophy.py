from logic.trophies.abstract_trophy import AbstractTrophy


class ActionTrophy(AbstractTrophy):

    def __init__(self, name, description, image, action_type, action_count):
        super().__init__(name, description, image)
        self.action_type = action_type
        self.action_count = action_count

    def check(self, games):
        actions_sum = 0
        for game in games:
            game_rounds = game["rounds"]
            for r in list(game_rounds.keys()):
                round = game_rounds.get(r)
                for p in list(round.keys()):
                    type_actions = [a for a in round.get(p).get("actions")
                                    if a == self.action_type]
                    actions_sum = actions_sum + len(type_actions)
        if actions_sum > self.action_count:
            return True
        return False
