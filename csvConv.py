#!/usr/bin/python
# CSV -> HTML

from bottle import route, run
import sys
import csv

#Open CSV file
reader = csv.reader(open(sys.argv[1],'rU'))

@route('/shownode/<name>')
def index(name):
#initialize Z
	z= ""
#make html into table
	z+=	'<table>'
	z+=	'<tr>'
	for row in reader:
		for column in row:
			z+= '<td>' + column + '</td>'
	z+=		'</tr>'
	#close table tag
	z+=	'</table>'
	return z
run(host='localhost', port=8080)

