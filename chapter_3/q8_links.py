"""This program links.py that takes URL of a webpage as argument and prints all the URLs linked from that webpage. """



import urllib
import re
def links(url):
    url1=urllib.urlopen(url)
    links=re.findall('http://[\w\d\s\.-]+.html',url1)
    for i in links:
	print i
	#inks1='www'+i[8:]
       #for j in links
	#   print j


links('http://python.org')
    
