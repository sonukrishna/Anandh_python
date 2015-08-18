"""this program prints the external ip of my system """


import urllib
response=urllib.urlopen('http://httpbin.org/get')
ip=response.header['Origin']
print ip
