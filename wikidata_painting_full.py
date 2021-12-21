import requests
import json
import pandas as pd
import time
from os.path import exists

# make this directoy  wikidata_q_data in the same place the script runs

#load in all the QIDs collected
qnumbers = json.load(open('qidsfull.json'))
url = "https://www.wikidata.org/wiki/Special:EntityData/"
# qnumbers = ['Q3305213', 'Q860861', 'Q11060274']

all_properties = {}
counter = 0

for qnum in qnumbers:

	counter=counter+1

	# this is where it will save it, with the directory
	new_file_name = f'wikidata_q_data/{qnum}.json'


	# test to see if we have this file already, if so skip
	if exists(new_file_name):
		print('Skipping', qnum)
		continue


	useurl = url + qnum + '.json'

	headers = {
		'Accept' : 'application/json',
		'User-Agent': 'USER databud - State of Art props '
	}

	print ('Starting ',useurl)
	time_start = time.time()

	r = requests.get(useurl, headers=headers, timeout=None)

	time_end = time.time()

	print('It took',time_end-time_start,'seconds, there are', len(qnumbers) - counter, 'left to do')

	data = json.loads(r.text)

	# write it out
	json.dump(data,open(new_file_name,'w'),indent=2)





