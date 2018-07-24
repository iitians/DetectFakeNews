import json
import newspaper
from newspaper import Article
import requests
import unidecode
import urllib

webSearchKeyA = "c7e39ef5a9a44d8cb35d00f7a8854ed6"
webSearchKeyB = "3c30ceeaae95429880730179e42f5720"
azureApiHeaders = {}
azureApiHeaders["Ocp-Apim-Subscription-Key"] = webSearchKeyA

baseQueryUrl = "https://api.cognitive.microsoft.com/bing/v7.0/search"
def makeQueryUrl(query, count=None, offset=None, mkt="en-US", safesearch=None):
    if (query is None):
        query = "pizzagate"
    queryParts = {}
    queryParts["q"] = query

    if (count is not None):
        queryParts["count"] = str(count)
    
    if (offset is not None):
        queryParts["offset"] = str(offset)
    
    if (mkt is not None):
        queryParts["mkt"] = str(mkt)
    
    if (safesearch is not None):
        queryParts["safesearch"] = str(safesearch)
    
    print(queryParts)
    return baseQueryUrl + "?" + urllib.urlencode(queryParts)


def getArticlesForQuery(query):
    results = []
    myQueryUrl = makeQueryUrl(query, count=100)
    req = requests.get(myQueryUrl, headers=azureApiHeaders)
    apiOutput = json.loads(req.content)
    webResults = apiOutput["webPages"]["value"]
    
    for i in xrange(0, len(webResults)):
        webResultUrl = webResults[i]["url"]
        results.append(webResultUrl)
        return
    return results

