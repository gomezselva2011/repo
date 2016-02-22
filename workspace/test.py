
import urllib
f = urllib.urlopen("http://nuevaya.com.ni")
s = f.read()
f.close()

from bs4 import BeautifulSoup
soup = BeautifulSoup(s, 'html.parser')
for article in soup.find_all('article'):
    print(article.get('id'))