
"""
//www.python.org/psf/license/
@author: gy18par
"""

# -*- coding: utf-8 -*-
# __version__ 1.0.0


# As a final touch, webscrapping can be introduced....


# Requesting page with table data
page=requests.get("http://www.geog.leeds.ac.uk/courses/computing/practicals/python/web/scraping-intro/table.html")
content = page.text


# Highlighting tabular ID data
table=soup.find(id="datatable")


# Cycling through all elements and looping
trs = table.find_all('tr')
for tr in trs:


# Inserting text
    tds = tr.find_all("td")
for td in tds:
    print (td.text)
