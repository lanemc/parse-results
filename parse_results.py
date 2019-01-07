#coding: utf-8

import csv
import pandas as pd

finalDict = {}

with open('results.txt', 'r') as f:
	# The following line of code is dependent on the structure of the results from running broken-link-checker (blc), which contain an empty line in between the summary of a link tree and the next root link.
	# Transform the data into lists that begin with a root link and end with an empty line.
	lines = list(map(lambda line: line.split('\n')[:-1],f.read().split('\n\n')))
	# Add the lists into a dictionary using the root link as the keys and the child links as the values
	finalDict = dict((elem[0],elem[1:]) for elem in lines)
	# Filter out identified failed redirects
	finalDict = {k: [x for x in v if not any(item in x for item in ['├───OK───', 'https://math.umn.edu/about/memoriam', 'https://math.umn.edu/research/combinatorics', 'https://math.umn.edu/5309694', 'http://oit-drupal-prd-web.oit.umn.edu/', 'http://www.myu.umn.edu/', 'https://www.myu.umn.edu/', 'http://www.myu.umn.edu', 'https://math.umn.edu/NA', 'www.linkedin.com', 'http://www.fox.temple.edu/mcm_people/'])] for k, v in finalDict.items()}
	# Replace '├─BROKEN─' with '' to clean the data
	val = '├─BROKEN─'
	for k, v in finalDict.items():
		finalDict[k] = [x.replace(val, '').strip() for x in v]
	# Remove dictionary keys (root links) that have no values
	finalDict = {k:v for k,v in finalDict.items() if len(v) > 0}


# Create a DataFrame from finalDict using the dictionary keys as column headers and the Series method, which allows the transfer of the list of dictionary values into DataFrame rows.
df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in finalDict.iteritems() ]))

print(df)

df.to_csv('new.csv', sep='\t', index=False)

#finalDf = pd.read_csv('new.csv', encoding='ascii')
df.to_html('index.html')

