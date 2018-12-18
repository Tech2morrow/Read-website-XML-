from urllib.request import urlopen
response = urlopen('http://www.google.com')
html = response.read()
print(html)
