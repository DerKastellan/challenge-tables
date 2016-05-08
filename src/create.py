#!/usr/bin/env python3

from parser import parseTables
from tables import ChallengeTable
from output import createHtml
import sys

def parseArgs():
    if len(sys.argv) < 2:
        raise ValueError()
    type   = sys.argv[1]
    if type not in { "html", "pdf" }:
        raise ValueError()

    levels = sys.argv[2:]
    return type, list(map(int, levels))


if __name__ == "__main__":
    uri = "http://dnd.wizards.com/products/tabletop/dm-basic-rules"

    print("... parsing table content from URI", uri, file=sys.stderr)
    thresholds, multipliers = parseTables(uri)
    print("... parsing table content from URI done", file=sys.stderr)

    print("... computing challenge table", file=sys.stderr)
    table = ChallengeTable(thresholds, multipliers)

    print("... outputting HTML challenge table", file=sys.stderr)

    type, levels = parseArgs()
    table = table.compute(levels)
    html  = createHtml(table)

    if type == "html":
        print(html)
    else:
        print("PDF not yet implemented", file=sys.stderr)
