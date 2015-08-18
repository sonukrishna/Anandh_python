"""The program should accept a URL as argument, download it and save it with the basename of the URL """


import os
import urllib
def wget(url):
    if url[-1]=='/':
	basename='index.html'
    else:
	basename=url.split('/')[-1]
    print "saving",url,"as",basename 
    urllib.urlretrieve(url,os.getcwd()   +'/'+basename)

url='http://docs.python.org/tutorial/interpreter.html'
url1='http://docs.python.org/tutorial/'
wget(url)
wget(url1)
