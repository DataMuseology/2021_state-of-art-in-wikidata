#sparql + how to work with the sparql request through JSON
import requests
import json
from urllib.parse import urlparse
import os

#import the request library bc requesting form website
#define the url we want to go to
#define the parameters we want to pass to the url
#inititate the request


#SPARQL query to identify all the QID's with the property P31 "instance of"
url = "https://query.wikidata.org/sparql"

#insert your SPARQL query here (copy and paste) between """
sparql = """
SELECT ?item WHERE {
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
        ?item p:P31/ps:P31/wdt:P279* wd:Q3305213.
}
"""

params = {
    'query' : sparql
}

#need to tell it to send data back as JSON
headers = {
    'Accept' : 'application/json',
    'User-Agent': 'USER databud - State of Art ' #to be changed based on individual
}

r = requests.get(url, params=params, headers=headers)
# print(r.text)

data = json.loads(r.text)

#   "results" : {
#     "bindings" : [ {
#       "item" : {

qids=[]
for results in data['results']['bindings']:

    # print(json.dumps(results,indent=3))
    # print(results['item']['value'])
    urls = (results['item']['value'])

    last_path_fragment = urlparse(urls).path.rstrip('/').split('/')[-1]
    # print(last_path_fragment)
    qids.append(last_path_fragment)

#create JSON file with all QIDS
with open('qidsfull.json','w') as jsonout:
    json.dump(qids,jsonout)
