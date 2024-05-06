import requests as req
from fake_useragent import UserAgent

url = "https://webmail.life.nthu.edu.tw/~labcli/"
ua = UserAgent(browsers=['edge', 'chrome', 'firefox', 'safari'])
headers = {"User-Agent":ua.random}

res = req.get(url+'image', headers=headers)
print("url : ", url+'image')
print(res.content)
