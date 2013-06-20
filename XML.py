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
	
	return ET.fromstring(xml)


def indexTree (root):
	indexedTreeHelper = [] 		# ['XML', 'THU', 'Team' ...]
	for child in root.iter():
		indexedTreeHelper.append(child.tag)

	return indexedTreeHelper


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


root = XML_read('RunXML.in', sys.stdout)
#print ElementTree.dump()

indexedTree = indexTree(root)
#print indexedTree

searchPattern = indexTree(root[1])
print searchPattern 

treeroot = root[0].tag   # THU
patternParent = searchPattern[0]
patternChild = searchPattern[1]
#for country in root.findall('country'):


#print list(root)