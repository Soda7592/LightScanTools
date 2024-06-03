import requests as req
from random import randint
from bs4 import BeautifulSoup

def getErrorPage(url) :
    r = randint(7, 987651)
    res = req.get(url + str(r))
    if(res.status_code != 404) :
        getErrorPage(url)
    else :
        #print(res.text)
        return res.text

def GuessWebServer(res) :
    if ("<h1>Not Found</h1>" in res.text) : 
        return "Apache"
    elif("404 Not Found" in res.text or "404 Page Not Found" in res.text) :
        return "Nginx"
    elif("HTTP Error 404 - File or directory not found") :
        return "IIS"
    elif("HTTP Error 404.0 - not Found") :
        return "IIS + ASP.NET"

#res = req.get(url + str(r))
getErrorPage('https://www.nthu.edu.tw/')
url = input("input the url with prptocol(Ex: https://example.com) > ")

r = getErrorPage(url)
soup = BeautifulSoup(r, 'html.parser')
#print(soup)

print("This website is a **", GuessWebServer(soup), "** web server possibly.")
