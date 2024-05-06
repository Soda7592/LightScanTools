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
    
'''
for i in common :
    res = req.get(url + '/' + i, headers=headers)
    print("path : ", i, " status_code : ", res.status_code)
'''


def UrlPathTravel(start, end, thn):
    for i in range(start, end) :
        time.sleep(0.15)
        headers = {"User-Agent":ua.random}
        try :
            res = req.get(url + str(common[i]), headers=headers)
            print(f"path {url} + {str(common[i])}:", res.status_code, f"   {thn}")
        except Exception as e:
            print(e)    
    '''
    for i in range(10) :
        time.sleep(0.15)
        print(i)
    '''

index = Make_wordlistIndex(3)

def ThrStart() :
    l = []
    for i in range(len(index)-1) :
        print(index[i], index[i+1])
        l.append(threading.Thread(target=UrlPathTravel, args=(index[i], index[i+1], i, )))
    for i in l:
        try :
            i.start()
        except Exception as e:
            print(e)  
#a = threading.Thread(target=UrlPathTravel, args=(index))
#threadsList = ThrStart()
ThrStart()
#print(threadsList)
#print(index) 






