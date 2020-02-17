import inflection
import bs4
import requests

r = requests.get('http://api.dailysmarty.com/posts')
rAsObject = r.json()
ps = rAsObject['posts']

for p in ps:
    postSplit = p['url_for_post'].split('/')
    lastElement = postSplit[-1]
    readableTitle = inflection.titleize(lastElement)
    print(readableTitle)

