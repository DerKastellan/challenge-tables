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
        self.parseTable(table)

    def parseTable(self, table):
        self.table = {}
        for label, multiplier in table:            
            multiplier = float(multiplier.replace("x ", "").replace("× ", ""))
            for number in self.extractList(label):
                self.table[number] = multiplier

    def extractList(self, label):
        def extractRangeList(label, separator):
            values = label.split(separator)
            values = list(map(int, values))
            values = values[0], values[1] +1 # ranges class is non-inclusive
            values = list(range(*values))
            return values

        if "or more" in label:
            value = label.replace(" or more", "")
            value = int(value)
            self.max = value
            return [value]
        elif "–" in label:
            return extractRangeList(label, "–")
            return values
        elif "-" in label:
            return extractRangeList(label, "-")
        else:
            return [int(label)]

    def get(self, numberOfEnemies):
        if numberOfEnemies < 1:
            raise ValueError()
        elif numberOfEnemies > self.max:
            return self.table[self.max]
        else:
            return self.table[numberOfEnemies]
