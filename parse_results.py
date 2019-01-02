#coding: utf-8

import csv
import pandas as pd
import re

finalDict = {}

with open('results.txt', 'r') as f:
	# The following line of code is dependent on the structure of the results from running broken-link-checker (blc), which contain an empty line in between the summary of a link tree and the next root link.
	# Transform the data into lists that begin with a root link and end with an empty line.
	lines = list(map(lambda line: line.split('\n')[:-1],f.read().split('\n\n')))
	# Add the lists into a dictionary using the root link as the keys and the child links as the values
	finalDict = dict((elem[0],elem[1:]) for elem in lines)
	# Filter out identified failed redirects
	finalDict = {k: [x for x in v if not any(item in x for item in ['├───OK───', 'https://math.umn.edu/about/memoriam', 'https://math.umn.edu/research/combinatorics', 'https://math.umn.edu/5309694', 'http://oit-drupal-prd-web.oit.umn.edu/', 'http://www.myu.umn.edu/', 'https://www.myu.umn.edu/', 'http://www.myu.umn.edu', 'https://math.umn.edu/NA', 'www.linkedin.com', 'http://www.fox.temple.edu/mcm_people/', 'https://math.umn.edu/seminars/past-seminars-series/MCFAM-Seminar/MCIM-Industrial-Problems-Seminar/'])] for k, v in finalDict.items()}
	# Remove dictionary keys (root links) that have no values
	finalDict = {k:v for k,v in finalDict.items() if len(v) > 0}

if ".*https://math.umn.edu/seminars/past-seminars-series/MCFAM-Seminar/MCIM-Industrial-Problems-Seminar/.*" in finalDict:
	del finalDict

#for k in finalDict.keys():
#	if k.contains('https://math.umn.edu/seminars/past-seminars-series/MCFAM-Seminar/MCIM-Industrial-Problems-Seminar/'):
#		dic.pop(k)
print(finalDict)

# Create a DataFrame from finalDict using the dictionary keys as column headers and the Series method, which allows the transfer of the list of dictionary values into DataFrame rows.
df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in finalDict.iteritems() ]))

#df = df.astype(str)
#df.applymap(lambda x: re.sub('├─BROKEN─','',x))

#print(df)
# Declare the target and replacement values for NaT strings
#findS = ['├───OK───']
#replaceS = ['']

# Replace NaT values with an empty string
#def removeNonAscii(col):
#        df[[col]] = df[[col]].replace(findS, replaceS)

#removeNonAscii(df)

#df.to_html('index.html')

df.to_csv('new.csv', sep='\t', index=False)
