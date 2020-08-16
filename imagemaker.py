import os
from bs4 import BeautifulSoup

doc = open('template.html', 'r').read()

soup = BeautifulSoup(doc, 'html.parser')
command_string = '"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --screenshot --window-size=1000,1000 --default-background-color=0 template.html'

print(soup.find('div'))
