# Getting introduced to BS4
from bs4 import BeautifulSoup

# easy html code to work on
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
# 1. Create a BeautifulSoup variable
doc = BeautifulSoup(html_doc,'html.parser')
# 2. Work on it
print(doc.prettify())

# Ways to navigate tag structure:
print(doc.title) # Title is a html tag
print(doc.title.name) # Name of the tag is title
print(doc.title.string) # String of the tag is the content
print(doc.title.parent.name) # Its parent name is head
print(doc.p) # p is another html tag
print(doc.a) # a is another html tag

# Methods for finding elements
print(doc.find_all('a'))
print(doc.find('p'))

for ref in doc.find_all('a'):
    print(ref.get('href')) # Ref is ResultSet object
# In the documentation of BeatifulSoup we can see ResultSet type is bascially a list
# which keep track of the SoupStrainer that created it, and SoupStrainer is a common
# link for the find methods

print(doc.get_text())

    
#with open(html_doc,'r') as f:
#    doc = BeautifulSoup(f,'html.parser')
# Reminder the with sintax means we do 2 things:
# 1: Calling __enter__ to open the file 
# 2: Calling __exit__ to close the file
# It helps us simplify exceptions management
    

# Modifying elements
tag = doc.title
print(tag)
tag.string = 'hello'
print(tag)

# Finding multiple elements
tags = doc.find_all('p')
for tag in tags:
    print(tag)
    
# Types of elements we can find [bs.element.]:
# 1. Tag: every html element (title, head, body, table, a, p, etc.)
#   1.1 Name: Every Tag has a name which can be changed
#   1.2 Attributes: id, class, href, etc.
# 2. NavigableString: a python string with some extra methods, used for the text contained in the html
# 3. BeautifulSoup: it represents the parsed document it can be treated as a Tag most of the times
# These 3 above are the more common types we are going to encounter