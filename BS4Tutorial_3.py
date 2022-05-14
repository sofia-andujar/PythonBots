# We have seen how to navigate, but searching is going to be key

from bs4 import BeautifulSoup
import re # regular expressions in python

# So once more:
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
doc = BeautifulSoup(html_doc,'html.parser')

# 1. We have the .find() and .find_all() methods 
for a in doc.find_all('a'):
    print(a.attrs['href'])

# This find all elements which start with b
for tag in doc.find_all(re.compile("^b")):
    print(tag)
    print(tag.name)

# We can give a list as an argument
for tag in doc.find_all(['a','b']):
    print(tag.name)

# Some notes:
# The find all looks through all descendants
# We can give as an input:
# the name of a tag ('a','title',etc.),
# keyword like id (id='link2', class='sister', id=True)
# multiple keywords like hred='link1', class='sister (together)
# class is a reserved word in python, so we use class_ in bs4
# if there's an attribute that won't work try this sintax: attrs={"class": "sister"}

# There are more methods like: find(), find_parent(), find_parents(), etc.
# their behaviour is similar to the navigating methods so no need of further explanation