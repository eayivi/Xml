#
#
#

import xml.etree.ElementTree as ET
import sys


def XML_read(r, w):
	freader = open('RunXML.in', 'r')

	line = freader.readline()
	xml = line

	while line != "":
		line = freader.readline()
		xml += line
		#print "LINE = " + line

	xml = "<XML>" + xml + "</XML>"

	#print xml

	root = ET.fromstring(xml)

	#print root.findall("THU")
	
	print root[0].findall("Team1")
	
	l = root.findall("Team3")







'''	
	for i in tree:
		print "child: " + str(i)
		for j in i:
			print "grandchild: " + str(j)
			for k in j:
				print "2gc: " + str(k)
'''
	#tree2 = ET.fromstringlist(tree)


	#print tree2

XML_read('RunXML.in', sys.stdout)
