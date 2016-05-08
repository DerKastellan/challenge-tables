#!/usr/bin/env python3

from data.tables import XpThreshold


from lxml import html


def parseTables(uri):
    doc = html.parse(uri)
    
    xpThresholds = extractXpThresholdTable(doc)

    return xpThresholds


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

    return XpThreshold(result)

def safeInt(x):
    try:
        clean = x.strip().replace(",", "")
        return int(clean)
    except ValueError:
        return None

if __name__ == "__main__":
    test = parseTables("http://dnd.wizards.com/products/tabletop/dm-basic-rules")
    print("20 HARD", test.get(20, XpThreshold.HARD))
