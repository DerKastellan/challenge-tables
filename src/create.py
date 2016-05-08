#!/usr/bin/env python3

from parser import parseTables
from tables import ChallengeTable


if __name__ == "__main__":
    uri = "http://dnd.wizards.com/products/tabletop/dm-basic-rules"

    print("... parsing table content from URI", uri)
    thresholds, multipliers = parseTables(uri)
    print("... parsing table content from URI done")

    print("... computing challenge table")
    table = ChallengeTable(thresholds, multipliers)
    table.compute([2, 2, 3, 3])
    table.compute([5, 5, 5, 5, 5])
