from bs4 import BeautifulSoup

import requests

def scraplinks(url = "https://aainaeiqbal.co.in/category/all-posts/",debug=0):
    
    links = []   
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    h2s=soup.find_all("a")

    
    for x in h2s:
        #print(x['href'])
        #print(x.a.string)
        #links[x.a.string]=x['href']
        links.append(x['href'])
    
    if links==[]:
        print("using html5parser")
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html5lib")
        h2s=soup.find_all("a")
        for x in h2s:
            links.append(x['href'])
    
    
    
    if debug==1:
        print("url= ",url)
        print("Content=",soup)
        print("Links= ",h2s)
    return links
print('scrript is runnin')
#az= scraplinks(url = "https://aainaeiqbal.co.in/category/all-posts/")
#print(az)
