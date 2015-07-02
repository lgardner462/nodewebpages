#!/usr/bin/python
# CSV -> HTML

import sys
import csv

#Open CSV file
	reader = csv.reader(open(sys.argv[1],'rU'))

#Make output html file
	htmlfile = open(sys.argv[2],"w")

#make html into table
	htmlfile.write('<table>')

	htmlfile.write('<tr>')
	for row in reader:
		for column in row:
			htmlfile.write('<td>' + column + '</td>')
		htmlfile.write('</tr>')
	#close table tag
	htmlfile.write('</table>')


