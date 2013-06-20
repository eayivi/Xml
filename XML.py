#
#
#

import xml.etree.ElementTree as ET

freader = open('RunXML.in', 'r')
fwriter = open('RunXML.in2', 'w')
freader2 = open('RunXML.in2', 'r')

line = freader.readline()
xml = line

while line != "":
	line = freader.readline()
	xml += line
	print "LINE = " + line

xml = "<XML>" + xml + "</XML>"

print xml

tree = ET.fromstring(xml)


root = tree.getroot()


children = list(root)
children1 = list(children[0])

print children
print children1

