from newspaper import Article
import requests

# Extract Article object from valid URL
def getURl() -> Article:
    articleURL = input("Paste your article's URL: ")
    notGot = True
    while(notGot):
        try:
            requests.get(articleURL)
            notGot = False
        except:
            articleURL = input("Invalid URL, try again: ")
            notGot = True
    return Article(articleURL)

# Get main text body
def getText(a : Article):
    a.download()
    a.parse()
    return a.text

getURl()