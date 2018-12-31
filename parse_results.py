import csv
import pandas as pd


finalDict = {}

with open('link_checker_result.txt', 'r') as f:
	lines = list(map(lambda line: line.split('\n')[:-1],f.read().split('\n\n')))
	finalDict = dict((elem[0],elem[1:]) for elem in lines)
	df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in finalDict.iteritems() ]))
	#df = pd.DataFrame({k : pd.Series(v) for k, v in finalDict.iteritems()})

names = df.columns
print(names)

# Declare the target and replacement values for NaT strings
#findS = ['NaN']
#replaceS = ['']

# Replace NaT values with an empty string
#def removeNaN(col):
#        df[col] = df[col].replace(findS, replaceS)

#removeNaN(df)

#print(df)

#df.to_csv('new.csv', sep='\t', index=False)
#new_df = pd.read_csv('new.csv')
#print(new_df)

#def search(values, searchFor):
#	for k in values:
#		for v in values[k]:
#			if searchFor in v:
#				return k
#

#def search(finalDict, lookup):
#	for key, value in finalDict.items():
#		for v in value:
#			if lookup in v:
#				return key

#print search(finalDict, 'BROKEN')

#with open('this_out.txt', 'w') as csv_file:
#	writer = csv.writer(csv_file)
#	for key, value in finalDict.items():
#		writer.writerow([key, value])


#print(finalDict)

#		with open('this_out.txt', 'w') as f2:
#			for line in result_list:
#				f2.write(line)
#mydict = []

#with open('result.txt', 'r') as f:
#	mylist = f.readlines().replace("\n", '$$$')
#	for line in mylist:
#		mydict.append(line)
        #with open('out.txt', 'w') as f2:
        #        name_string = f.read()
        #        #name_string = name_string.replace('"', '')
        #        items = name_string.split('\n \n')
        #        for line in items:
	#		mydict.append(line)
	#		f2.write(line)
#print(mydict)
                        #f2.write(lines)

#with open('result.txt') as f:
#	print([i.strip().split('Getting') for i in f])

