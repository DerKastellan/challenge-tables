#!/usr/bin/env python3

from parser import parseTables
from tables import ChallengeTable
from output import createHtml, createPdf
import sys

def parseArgs():
    def convertPartyString(x):
        # "5 3 3 2" => [5, 3, 3, 2]
        return list(map(int, x.strip().split(" ")))

    if len(sys.argv) < 3:
        raise ValueError()
    
    type = sys.argv[1]
    if type not in { "html", "pdf" }:
        raise ValueError()

    path   = sys.argv[2]
    levels = list(map(convertPartyString, sys.argv[3:]))

    return type, path, levels


if __name__ == "__main__":
    uri = "http://dnd.wizards.com/products/tabletop/dm-basic-rules"

    print("... parsing table content from URI", uri, file=sys.stderr)
    thresholds, multipliers = parseTables(uri)
    print("... parsing table content from URI done", file=sys.stderr)

    print("... computing challenge table", file=sys.stderr)
    table = ChallengeTable(thresholds, multipliers)

    type, path, levels = parseArgs()

    tables  = list(map(table.compute, levels))
    content = list(zip(levels, tables)) # [ ( <party levels>, <challenge table> ) ]
    html    = createHtml(content)

    if type == "html":
        print("... writing challenge table as HTML to '{}'".format(path), file=sys.stderr)
        with open(path, encoding="utf-8", mode="w") as f:
            f.write(html)
    else:
        print("... writing challenge table as PDF to '{}'".format(path), file=sys.stderr)
        createPdf(path, html)

    print("... done", file=sys.stderr)
