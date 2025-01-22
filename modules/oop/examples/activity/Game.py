from modules.oop.examples.activity.GroupActivity import GroupActivity


class Game(GroupActivity):
    count = 1

    def __init__(self, name, kind, rules):
        GroupActivity.__init__(self, name, kind)
        self.rules = rules

    def add_rule(self, rule):
        self.rules.append(rule)

    def present_rules(self):
        return f'Regras do Jogo: \n' + " ".join(self.rules)

    def present(self):
        return f'Jogo: {self.name}\n{self.present_rules()}'