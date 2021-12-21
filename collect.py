
# put the rest of this into another script
# load each json file like this

import glob
import json
import csv


all_properties = {}
for filename in glob.glob('wikidata_q_data/*.json'):

    data = json.load(open(filename))

    qnum = data['entities'].keys()
    qnum =list(qnum)
    qnum =qnum[0]


    properties = list(data['entities'][qnum]['claims'].keys())
    # print(properties)

    for p in properties:
        if p not in all_properties:
            all_properties[p] = 0
        all_properties[p]+=1


# print(all_properties)
dict1= all_properties
sorted_tuples = sorted(all_properties.items(), key=lambda item: item[1], reverse=True)
# print(sorted_tuples)
sorted_dict = {k: v for k, v in sorted_tuples}
print(sorted_dict)


# #write to csv for load into Tableau for Viz
keys, values = [], []

for key, value in sorted_dict.items():
    keys.append(key)
    values.append(value)
 
with open('proplistsorthalf.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(keys)
    csvwriter.writerow(values)