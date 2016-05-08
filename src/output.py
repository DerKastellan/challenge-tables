def createHtml(challengeTable):
    def convertRow(index, row):
        row = list(map(lambda x: "<td>{}</td>".format(x), row))

        indent  = "\t\t"
        rowHead = "{indent}<tr{style}>\n{indent}".format(indent=indent,style=rowStyle(index))
        rowTail = "\n{indent}</tr>".format(indent=indent)
        rowSep  = "\n{indent}".format(indent=indent)

        return rowHead + rowSep.join(row) + rowTail

    def rowStyle(index):        
        if index % 2 == 0:
            # even lines: add silver background
            return ' bgcolor="silver"'
        else:
            # odd lines: do nothing
            return "" 

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
    <table>
        <caption>Challenge Table</caption>
        <tr>
        <th>Number of Enemies</th>
        <th>Easy</th>
        <th>Medium</th>
        <th>Hard</th>
        <th>Deadly</th>
        </tr>
{tableRows}
    </table>
</body>
</html>"""
    

    rows    = [ convertRow(index, challengeTable[index]) for index in range(0, len(challengeTable)) ]
    content = "\n".join(rows)

    return html.format(tableRows=content, title="Challenge Table")
