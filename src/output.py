def createHtml(challengeTables):
    def convertRow(index, row):
        row = list(map(lambda x: "<td>{}</td>".format(x), row))

        rowHead = "        <tr{style}>\n            ".format(style=rowStyle(index))
        rowTail = "\n        </tr>"
        rowSep  = "\n            "

        return rowHead + rowSep.join(row) + rowTail

    def rowStyle(index):        
        if index % 2 == 0:
            # even lines: add silver background
            return ' bgcolor="silver"'
        else:
            # odd lines: do nothing
            return ""

    def createDescription(levels):
        desc = "For a party with individual levels of: " + ", ".join(map(str, levels))
        return '<td colspan="5">{}</td>'.format(desc)
    def createTable(entry):
        levels, challengeTable = entry # unpack tuples
        rows                   = [ convertRow(index, challengeTable[index]) for index in range(0, len(challengeTable)) ]
        content                = "\n".join(rows)

        table = \
"""    <table>
        <caption>Challenge Table</caption>
        <tr>{description}</tr>
        <tr>
            <th>Number of Enemies</th>
            <th>Easy</th>
            <th>Medium</th>
            <th>Hard</th>
            <th>Deadly</th>
        </tr>
{tableRows}
    </table>
"""
        return table.format(tableRows=content, description=createDescription(levels))

    html = \
"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <style>
        table   {{width: 800px; text-align: center;}}
        caption {{font-size: xx-large; font-weight: bold;}}
        th      {{width: 160px;}}
    </style>
</head>
<body>
{tables}
</body>
</html>"""
    
    content = "    <br/><br/>\n".join(map(createTable, challengeTables))

    return html.format(tables=content, title="Challenge Table")
