import requests
from bs4 import BeautifulSoup, Comment

def fetch_html_comments(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    return comments

url = input("Input a url to fetch comments > ") #'https://www.mozilla.org/zh-TW/'
comments = fetch_html_comments(url)

for idx, comment in enumerate(comments, start=1):
    print(f"Comment {idx}: {comment}")
