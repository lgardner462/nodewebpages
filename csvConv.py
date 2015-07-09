#!/usr/bin/python
# CSV -> HTML

from bottle import route, run, template, static_file
import sys
import csv

#Open CSV file
reader = csv.reader(open(sys.argv[1],'rU'),skipinitialspace = True)

reader.next()
reader.next()
#Initialize Lists
nodeNames = []
nodeLoc = []
nodeNameAndLoc = []
nodeMac = []
csvFull = []
nameCSVZipped = []

#Zip first two columns into dictionaries
for row in reader:
	csvFull.append(row)	
	nodeNames.append(row[0])
	nodeLoc.append(row[1:2])
	nodeNameAndLoc.append(row[0:2])	
	nodeMac.append(row[10:11]) 	
nameLocZipped = dict(zip(nodeNames,nodeLoc))
nameMacZipped = dict(zip(nodeNames,nodeMac))
nameCSVZipped = dict(zip(nodeNames,csvFull))	
	
#route to node+<no> wildcard
#@route('/rack/node<no>')
#def index(no):
#	location=nameLocZipped['node'+str(no)] #Dictionary key gets node+<no>, location gets nameLocZipped[] value
#	output = template('how I display a node', no=no,location=location) #convert to html table	
#	return output

#show mac address for selected node
#@route('/mac/node<no>')
#def index(no):
#	location=nameMacZipped['node'+str(no)]
#	output = template('how I display a node', no=no,location=location) #convert to html table
#	return output
	

#Show nodes
#@route('/shownodes')	
#def shownodes():	
#	output = template('shownodes.tpl',csvFull=csvFull)
#	return output


#Top page
@route('/top')
def top():	
	output = template('top1.tpl',csvFull=csvFull)
	return output

#Routes to designated node's info
@route('/node<no>')
def index(no):
	location = nameCSVZipped['node'+str(no)]
	output = template('nodepage.tpl',no=no,location=location,nameCSVZipped=nameCSVZipped)
	return output

#Shows rack location for all nodes	
@route('/showrack')
def showrack():
	output = template('showrack.tpl',nameLocZipped=nameLocZipped)
	return output	

#Show mac address for all notes
@route('/showmac')
def showmac():
	output = template('showmac.tpl',nameMacZipped=nameMacZipped)
	return output	

#Downloads csv file
@route('/download<filename:path>')
def download(filename):
	return static_file(filename, root ='/home/Lawrence/git/nodewebpages',download=filename)

run(host='localhost') #Make sure this is last or else it won't load the pages after it

