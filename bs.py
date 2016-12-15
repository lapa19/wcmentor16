import urllib2
from bs4 import BeautifulSoup
url = urllib2.urlopen("http://www.imdb.com/chart/top")
content = url.read()
soup = BeautifulSoup(content)
title=soup.find_all("td",{"class":"titleColumn"})
rating=soup.find_all("td",{"class":"ratingColumn imdbRating"})
titles=[]
ratings=[]
for t in title:
    #get titles
	titles.append(t.find('a').getText())
for r in rating:
	#get ratings
	ratings.append(r.getText())

f=open('imdb.txt','w');
for l,r in zip(titles,ratings):
	f.write(l.encode('utf8'))
	f.write(r.encode('utf8'))
	f.write("\n")
