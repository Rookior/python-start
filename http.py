




# import urllib.request

# url="http://www.baidu.com"

# html = urllib.request.urlopen(url).read()
# print (html)

from urllib.request import urlopen

myURL = urlopen("https://www.runoob.com/")
print(myURL.read())
