#!/usr/bin/python
# CSV -> HTML

from bottle import route, run, template
import sys
import csv

#Open CSV file
reader = csv.reader(open(sys.argv[1],'rU'))



@route('/shownode/<name>')
def index(name):
#make html into table
	output = template('how I display a node', rows=reader)	
	return output
run(host='localhost')

