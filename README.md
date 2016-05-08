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
* lxml

## Running it

Currently it works as follows:

* clone the project
* change working dir into project
* `src/create.py html <list individual levels of party members>`
* this prints the HTML to stdout, redirect to file if needed
* all program output that is not data is stderr stream

Example: 

* `src/create.py html 5 5 5 5 4` (a party of 4 lv5s and 1 lv 4)

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
        <tr>
        <th>Number of Enemies</th>
        <th>Easy</th>
        <th>Medium</th>
        <th>Hard</th>
        <th>Deadly</th>
        </tr>
                <tr bgcolor="silver">
                <td>1</td>
                <td>1125</td>
                <td>2250</td>
                <td>3375</td>
                <td>4900</td>
                </tr>
                <tr>
                <td>2</td>
                <td>750</td>
                <td>1500</td>
                <td>2250</td>
                <td>3267</td>
                </tr>
                <tr bgcolor="silver">
                <td>3 - 4</td>
                <td>563</td>
                <td>1125</td>
                <td>1688</td>
                <td>2450</td>
                </tr>
                <tr>
                <td>7 - 8</td>
                <td>450</td>
                <td>900</td>
                <td>1350</td>
                <td>1960</td>
                </tr>
                <tr bgcolor="silver">
                <td>11 - 12</td>
                <td>375</td>
                <td>750</td>
                <td>1125</td>
                <td>1634</td>
                </tr>
                <tr>
                <td>15+</td>
                <td>282</td>
                <td>563</td>
                <td>844</td>
                <td>1225</td>
                </tr>
    </table>
</body>
</html>
```


