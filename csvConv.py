#!/usr/bin/python
# CSV -> HTML

from bottle import route, run, template
import sys
import csv

#Open CSV file
reader = csv.reader(open(sys.argv[1],'rU'))
for row in reader:
	text = row[0:2]
	

@route('/shownode/<name>')
def index(name):
#make html into table
	output = template('how I display a node', rows=text)	
	return output
	
run(host='localhost')

