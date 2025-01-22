from modules.oop.examples.activity.Game import Game


class BoardGame(Game):
    def __init__(self, name, kind, rules, cards):
        super().__init__(name, kind, rules)
        self.cards = cards
        super().add_rule("Regra 0")
        Game.add_rule(self, "Regra 0")

    def present_rules(self):
        return 'Regras do Board Game: \n' + '\n'.join(self.rules)