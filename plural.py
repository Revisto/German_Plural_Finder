
import requests
from bs4 import BeautifulSoup

url = "https://www.verbformen.com/declension/nouns/?w="
word=input()
url+=word
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)

with open("fname.txt", "w", encoding="utf-8") as f:
    f.write(str(text))

text=text[text.index('Plural'):text.index('Plural')+20]
die=text.index("die")
Pl="die "
while True:
    die+=1

    if text[die]=='\n' or (chr(47)) in text[die]:
        break
    Pl+=text[die]
print (Pl)
