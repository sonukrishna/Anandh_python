"""takes a URL as argument, downloads the
html from web and print it after stripping html tags."""


import os
import urllib
import re
def antihtml(url):
    if url[-1]=='/':
        basename='index.html'
    else:
        basename=url.split('/')[-1]
    print "saving",url,"as",basename
    urllib.urlretrieve(url,os.getcwd()   +'/'+basename)
    words=re.findall('>[^<]+<',url)
    for i in words:
	print i[1:-1]

antihtml('http://docs.python.org/tutorial/interpreter.html')
