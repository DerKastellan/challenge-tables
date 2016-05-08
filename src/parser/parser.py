#!/usr/bin/env python3

from data.tables import XpThresholds, Multipliers
from lxml import html
import re


def parseTables(uri):
    doc = html.parse(uri)
    
    xpThresholds = extractXpThresholdTable(doc)
    multipliers  = extractMultiplierTable(doc)

    return xpThresholds, multipliers


def findTableElementByCaption(doc, captionText):
    caption = doc.xpath("//caption[text()='{}']".format(captionText))[0]
    return caption.getparent()

def extractXpThresholdTable(doc):
    def safeInt(x):
        try:
            clean = x.strip().replace(",", "")
            return int(clean)
        except ValueError:
            return None
        
    table  = findTableElementByCaption(doc, "XP Thresholds by Character Level")
    rows   = [ tr for tr in table.xpath("tbody/tr") ]
    result = []

    for tr in rows:
        columns = tr.xpath("td/text()")
        # ignore level column
        columns = columns[1:]
        columns = list(map(safeInt, columns))

        result.append(columns)

    return XpThresholds(result)

def extractMultiplierTable(doc):
    pattern = re.compile("[0-9][0-9]?")

    def containsNumber(x):
        return pattern.search(x) is not None

    table  = findTableElementByCaption(doc, "Encounter Multipliers")
    result = []

    text = [ text for text in table.xpath("tbody/tr/td/text()") ]
    text = list(filter(containsNumber, text)) # filter out invalid
    labels      = text[0:][::2]
    multipliers = text[1:][::2]

    result = list(zip(labels, multipliers))

    return Multipliers(result)

def safeInt(x):
    try:
        clean = x.strip().replace(",", "")
        return int(clean)
    except ValueError:
        return None

if __name__ == "__main__":
    thresholds, multipliers= parseTables("http://dnd.wizards.com/products/tabletop/dm-basic-rules")
    print("20 HARD", thresholds.get(20, XpThresholds.HARD))
    print("ENEMIES 20 {}, 13 {}, 7 {}, 1 {}".format(*map(multipliers.get, [20, 13, 7, 1])))

