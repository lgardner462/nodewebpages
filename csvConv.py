#!/usr/bin/python
# CSV -> HTML

from bottle import route, run, template
import sys
import csv

#Open CSV file
reader = csv.reader(open(sys.argv[1],'rU'))
#Initialize Lists
nodeNames = []
nodeLoc = []
#Zip first two columns into dictionaries
for row in reader:
	nodeNames.append(row[0])
	nodeLoc.append(row[1:2])
	nodeZipped = dict(zip(nodeNames,nodeLoc))

#route to node+<no> wildcard
@route('/shownode/node<no>')

def index(no):
	location=nodeZipped['node'+str(no)] #Dictionary key gets node+<no>, location gets nodeZipped[] value
	output = template('how I display a node', no=no,location=location) #convert to html table	
	return output
	
run(host='localhost')

