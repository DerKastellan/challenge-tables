import math

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
        self.categories = []
        for label, multiplier in table:            
            multiplier = float(multiplier.replace("x ", "").replace("× ", ""))

            category = self.extractList(label)
            self.categories.append(category)

            for number in category:
                self.table[number] = multiplier

        self.categories = list(sorted(self.categories))

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

    def getCategories(self):
        return self.categories

class ChallengeTable:
    def __init__(self, thresholds, multipliers):
        self.thresholds  = thresholds
        self.multipliers = multipliers

        self.createRows()

    def createRows(self):
        def convertLabel(label):
            if len(label) > 1:
                return "{} - {}".format(label[0], label[-1])
            else:
                return str(label[0])

        labels = self.multipliers.getCategories()
        rows     = list(map(convertLabel, labels))
        rows[-1] = rows[-1] + "+"
        
        self.rows = list(zip(rows, map(lambda x: x[0], labels)))

    def compute(self, partyLevels):
        def computeBaseline(challenge):
            return sum([ self.thresholds.get(level, challenge) for level in partyLevels ])

        def computeValue(base, multi):
            return math.ceil(base / multi)


        easy   = computeBaseline(XpThresholds.EASY)
        medium = computeBaseline(XpThresholds.MEDIUM)
        hard   = computeBaseline(XpThresholds.HARD)
        deadly = computeBaseline(XpThresholds.DEADLY)

        baseline = [easy, medium, hard, deadly]

        result = []

        for label, minFoeThreshold in self.rows:
            multi = self.multipliers.get(minFoeThreshold)
            result.append([label] + list(map(lambda x: computeValue(x, multi), baseline)))

        return result

