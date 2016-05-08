class XpThresholds:

    EASY   = 0
    MEDIUM = 1
    HARD   = 2
    DEADLY = 3

    challenge = [ EASY, MEDIUM, HARD, DEADLY ]

    def __init__(self, tables):
        self.tables = tables

    def get(self, level, challenge):
        if level < 1 or level > 20:
            raise ValueError()

        if challenge not in self.challenge:
            raise ValueError()

        return self.tables[level-1][challenge]

class Multipliers:

    def __init__(self, table):
        self.table = table
