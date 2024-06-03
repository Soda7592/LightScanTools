import requests as req
from fake_useragent import UserAgent 
import threading
import time

common = open("WordlistForScanTool/small.txt", 'r').readlines()
common = [x.strip('\n') for x in common]
#dict_wordlist = []
#print(common)
#input()
url = input("Input a url > ")
ua = UserAgent(browsers=['edge', 'chrome', 'firefox', 'safari'])
headers = {"User-Agent":ua.random}
if url[len(url)-1] != '/' :
    url += '/'
print(url)
#res = req.get(url, headers=headers)
#print(res)

def Make_wordlistIndex(threads) :
    l = []
    copies = 0
    for i in range(threads-1) :
        l.append(copies)
        copies += len(common)//threads
    l.append(len(common)//threads + len(common)%threads + l[len(l)-1])
    l.append(len(common))
    return l


def UrlPathTravel(start, end, thn):
    for i in range(start, end) :
        time.sleep(0.15)
        headers = {"User-Agent":ua.random}
        try :
            print(url + str(common[i]))
            res = req.get(url + str(common[i]), headers=headers, timeout=4)
            if res.status_code == 200 :
                print(f"path {url}{str(common[i])} found ,", f"\033[31m {res.status_code}\033[0m ({len(res.content)}Bytes)")
                if b"Parent Directory" in res.content and b"Index of" in res.content :
                    print(f"\033[31m path {url}{str(common[i])} has Dierctory listing vuln\033[0m")
            #else :
                #print(f"path {url}/{str(common[i])}", res.status_code)
            #print(common[i], f"{thn} {i}")
        except Exception as e:
            print(e)    

index = Make_wordlistIndex(3)

l = []
for i in range(len(index)-1) :
    #print(index[i], index[i+1])
    t = threading.Thread(target=UrlPathTravel, args=(index[i], index[i+1], i, ))
    l.append(t)
    t.start()
for i in l:
    i.join()  

