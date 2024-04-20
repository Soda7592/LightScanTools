import requests as req

url = input("input a url > ")
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
HttpSecurityHeaders = ["Content-Security-Policy", "Strict-Transport-Security", "X-Content-Type-Options", "X-Frame-Options", "X-XSS-Protection"]
ExistKey = []
resHeader = ""
res = ""

print("Scanning...")

try :
    res = req.get(url, headers=headers)
except Exception as e :
    print(e)

if res.status_code != 200 :
    print("Connection Failed")
    print(f"Failed status code is {res.status_code}")    
else :
    resHeader = res.headers

for i in HttpSecurityHeaders :
    if i not in resHeader :
        print(f"There is not exists header : {i}")
    else :
        ExistKey.append(i)    

if len(ExistKey) != 0 :
    print("HTTP Headers : ")    

for i in ExistKey :
    print(f"\t**{i}**\t detected.")
    if i == "Content-Security-Policy" :
        if "default-src" in resHeader[i] :
            print("defalut-src has been detected.")  
    elif i == "Strict-Transport-Security" :
        if "includeSubDomains" in resHeader[i] :
            print("You might notice the subdomain, it could be browed by http protocol.")
        else :
            print("This web page might agnist the MITM Attack. You couldn't browse it by http.")
    
    elif i == "X-Content-Type-Options" :
        if "nosniff" in resHeader[i] :
            print("This webpage might avoid the MIME type nosniff")
        else :
            print("This Header might got some wrong configeration. And the MIME type sniff might work.")
    elif i == "X-Frame-Options" :
        if "DENY" in resHeader[i] :
            print("This web almost avoid the click-jacking")
        elif "SAMEORIGIN" in resHeader[i] :
            print("You need to pay attention to some web page which is same origin. It might click-jacking.")
    elif i == "X-XSS-Protection" :
        print("Your are recommand to change this header to CSP. It has been deprecated.")
    #elif i == "Content-Security-Policy" :
    #   if "default-src" in resHeader[i] :
