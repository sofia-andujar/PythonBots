# There are plenty of methods to find children elements, siblings, etc.
# Which we are going to prefer to as navigating the tree

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
doc = BeautifulSoup(html_doc,'html.parser')

# Let's see some strategies for navigating the tree:
# 1. Simply using tag names
title = doc.title
body = doc.body
bold = doc.body.b
link = doc.a

# 2. .contents and .children methods
head_contents = doc.head.contents
print(head_contents)
title_contents = doc.head.title.contents
print(title_contents) 
print(type(title_contents)) # Realize the type returned is a list
print(len(doc.contents))
# contents and children are for immediate descendants

# 3. .descendants 
for child in doc.head.descendants:
    print(child)
# The string ot the title is a child of the title so it's related to the head somehow
print(type(doc.children)) # list_iterator not list
print(len(list(doc.children)))
print(type(doc.descendants)) # generator
print(len(list(doc.descendants)))

# 4. .string
print(doc.head.title.string) # The string is title's child it is returned for the head too
print(doc.head.string)
print(doc.body.p.string)
print(doc.body.string) # If the tag contains multiple tags then output is none
for string in doc.body.stripped_strings: # But we can use .strings or .stripped_strings
    print(string)

# 5. We can go up as well with .parent or .parents
specific_content = doc.body.p 
print(specific_content.parent) # the parent is body so it prints the whole body
for parent in specific_content.parents:
    print(parent.name) # Outputs: body,html,document
    
# 6. We can move through siblings
body_a = doc.body.a
print(body_a) # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print(body_a.next_sibling) #, this is html text at the same tree level as a

for sibling in body_a.next_siblings:
    print(repr(sibling)) # using repr so we can visualize the '\n' characters
    
# 7. We can move through the document careless of the level os the tree we are in
for element in doc.head.next_elements:
    print(element.name) # there are plenty of lines with no name, the lines containing text



# We can also access websites with requests:
# webPage = requests.get('https://www.amazon.es/')
# print(webPage.text)
# doc = BeautifulSoup(webPage.text,'html.parser')
# print(doc.prettify())
