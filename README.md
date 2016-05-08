# Challenge Tables

The purpose of this project is to automate the process of making challenge tables for the world's greatest role-playing game.

## What is a Challenge Table

For determining the challenge of combat encounters in 5e we use XP values for calculating thresholds. These thresholds are then used for gauging how hard an encounter for a given party is.

There is, however, a problem. The math involved is not intuitive. The more monsters are added to an encounter, the higher the XP values gets. It gets multiplied but compared against the same threshold.

This is easy to fix, however. One simply needs to divide the values in a given table by the multiplier and one gets the amount of XP presenting the challenge threshold for this number of monsters.

## What this project is supposed to do

Making such Challenge Tables can become tedious by hand, requiring sitting around comparing values with a table and calculating the modified values. This project aims at producing a printable PDF of such a table for your perusal at the game table.

With a challenge table, encounter creation on the fly is easy. The rest is up to your imagination.

## Prerequisites

You need to have installed:
* python3
* lxml
* pdfkit

## Running it

Currently it works as follows:

* clone the project
* change working dir into project
* `src/create.py html <dest file> "<list individual levels of party members>" "<next list>"`

Example: 

* `src/create.py html out.html "6 6 6 6 5" ` (a party of 4 lv6s and 1 lv 5)

Result:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Challenge Table</title>
    <style>
        table   {width: 800px; text-align: center;}
        caption {font-size: xx-large; font-weight: bold;}
        th      {width: 160px;}
    </style>
</head>
<body>
    <table>
        <caption>Challenge Table</caption>
        <tr><td colspan="5">For a party with individual levels of 1xlv5, 4xlv6</td></tr>
        <tr>
            <th>Number of Enemies</th>
            <th>Easy</th>
            <th>Medium</th>
            <th>Hard</th>
            <th>Deadly</th>
        </tr>
        <tr bgcolor="silver">
            <td>1</td>
            <td>1450</td>
            <td>2900</td>
            <td>4350</td>
            <td>6700</td>
        </tr>
        <tr>
            <td>2</td>
            <td>967</td>
            <td>1934</td>
            <td>2900</td>
            <td>4467</td>
        </tr>
        <tr bgcolor="silver">
            <td>3 - 4</td>
            <td>725</td>
            <td>1450</td>
            <td>2175</td>
            <td>3350</td>
        </tr>
        <tr>
            <td>7 - 8</td>
            <td>580</td>
            <td>1160</td>
            <td>1740</td>
            <td>2680</td>
        </tr>
        <tr bgcolor="silver">
            <td>11 - 12</td>
            <td>484</td>
            <td>967</td>
            <td>1450</td>
            <td>2234</td>
        </tr>
        <tr>
            <td>15+</td>
            <td>363</td>
            <td>725</td>
            <td>1088</td>
            <td>1675</td>
        </tr>
    </table>

</body>
</html>
```


