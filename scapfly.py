# note: you can install beautifulsoup package through "$ pip install beautifulsoup4" command in your terminal
from bs4 import BeautifulSoup

html = """
<head>
  <title class="page-title">Hello World!</title>
</head>
<body>
  <div id="content">
    <h1>Title</h1>
    <p>first paragraph</p>
    <p>second paragraph</p>
    <h2>Subtitle</h2>
    <p>first paragraph of subtitle</p>
  </div>
</body>
"""

# build soup object from html text
soup = BeautifulSoup(html)
# then we can navigate the html tree via python API:
# for example title is under <head> node and under <> node

print(soup.head.title)
# <title class="page-title">Hello World!</title>

# further we can get the text attribute instead of this entire node:
print(soup.head.title.text)
# Hello World!

# or it's other attributes:
print(soup.head.title["class"])
# page-title