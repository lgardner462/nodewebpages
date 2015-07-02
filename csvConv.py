#!/usr/bin/python
# CSV -> HTML

from bottle import route, run, template
import sys
import csv

#Open CSV file
reader = csv.reader(open(sys.argv[1],'rU'))

nodeNameLoc = []
nodeNames = []
nodeLoc = []

for row in reader:
	nodeNames.append(row[0])
	nodeLoc.append(row[1:2])
	nodeNameLoc.append(row[0:2])

@route('/shownode/<nodeNames>')
def index(nodeNames):
#make html into table
	output = template('how I display a node', rows=nodeNameLoc)	
	return output
	
run(host='localhost')

