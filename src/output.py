def createHtml(challengeTable):
    def convertRow(row):
        row = list(map(lambda x: "<td>{}</td>".format(x), row))
        row = "\t<tr>\n\t" + "\n\t".join(row) + "\n\t</tr>"
        return row

    html = """
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
</head>
<body>
    <table>
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
    
    rows = "\n".join([ convertRow(row) for row in challengeTable ])

    return html.format(tableRows=rows, title="Something")
