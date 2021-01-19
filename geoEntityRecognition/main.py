import os
from extractLocationFromText import ExtractLocationFromText
from getIdentifer import getWikiRecord
from lxml import etree as et
import time
from writeHTML import writeToHTML

def loc_with_link(loc):
    return f'<a href="{loc.wikiID}">{loc.text}</a>' if loc.wikiID else f'<span style="color: #ff0000">{loc.text}</span>'


if __name__ == '__main__':

    testDataPath = "test_data/"
    parser = ExtractLocationFromText()
    testData = os.path.join(testDataPath, "fr_paris_a_Jerusalem.txt")
    text = open(testData, "r").read()
    foundLocations = parser.getLocationsFrench(text)
    counter = 0
    for loc in foundLocations:
        print(counter)
        loc.wikiID, loc.geonameID, loc.longitude, loc.latitude = getWikiRecord(loc.text, loc.language)
        if (counter==10):
            time.sleep(60)
            counter = 0
    
    # Adding paragraph tags for each line.
    englishText = ["<p>" + x + "</p>" for x in englishText.split("\n")]

    # Creating HTML file
    root = et.Element("html")
    head = et.SubElement(root, "head")
    body = et.SubElement(root, "body")
    title = et.SubElement(body, "h1")
    title.text = "The Tales of Magellan"

    # Adding a new paragraph for each line in englishText
    for line in englishText:
        elem = et.fromstring(line)
        body.append(elem)

    html_body = writeToHTML(text, foundLocations)
    html_content= """<html>
    <head></head>\n
    <body>\n<p>""" + html_body + """\n</p>\n</body>
    </html>"""

    f = open("fr_paris_a_Jerusalem.html", "w")
    f.write(html_content)
    f.close()
