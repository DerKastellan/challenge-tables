#!/usr/bin/env python3

from parser import parseTables
from tables import ChallengeTable
from output import createHtml
import sys

def parseArgs():
    args = sys.argv[1:]
    return list(map(int, args))


if __name__ == "__main__":
    uri = "http://dnd.wizards.com/products/tabletop/dm-basic-rules"

    print("... parsing table content from URI", uri, file=sys.stderr)
    thresholds, multipliers = parseTables(uri)
    print("... parsing table content from URI done", file=sys.stderr)

    print("... computing challenge table", file=sys.stderr)
    table = ChallengeTable(thresholds, multipliers)

    print("... outputting HTML challenge table", file=sys.stderr)

    levels = parseArgs()
    table  = table.compute(levels)

    print(createHtml(table))
