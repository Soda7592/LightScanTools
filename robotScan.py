import requests as req

#url = "https://www.nthu.edu.tw/"
url = input("Input the url > ")
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = ""
# print(common)
if url[len(url)-1] == '/' : 
    res = req.get(url + "robots.txt", headers=headers)
else :
    res = req.get(url + "/robots.txt", headers=headers)

def listRobotsurl():
    rob = res.content.decode("utf-8").split("\n")
    urlist = []
    for i in rob :
        if "Disallow" in i:
            if len(i[i.find("/"):]) > 1 :
                urlist.append(i[i.find("/")+1:-2].strip("\r").strip())
        elif "Allow" in i:
            if len(i[i.find("/"):]) > 3 :
                urlist.append(i[i.find("/")+1:-2].strip("\r").strip()) 
    return urlist

def MappingCommon() :
    common = open("WordlistForScanTool/wordlist.txt", "r").read()
    r = listRobotsurl()
    #print(r)
    potentialpath = []
    for i in r:
        if i in common :
            potentialpath.append(i)
    if len(potentialpath) > 0:
        print("The potential path had been found in /robots.txt :")
        for i in potentialpath :
            print(f"    **{i}**")
MappingCommon()

'''
print("Scanning ... \n")
try :
    res = req.get(url+"/robots.txt", headers=headers)
except Exception as e :
    print(e)

if res.status_code != 200 :
    print("Connect Faile.")
    print(f"Failed status code is {res.status_code}")
else :
    print(res.content.decode("utf-8"))
'''
