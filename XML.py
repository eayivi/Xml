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

def findPattern(parent, pattern, patternIndex) :
	if parent.tag == pattern[patternIndex] :
		patternIndex += 1
		if patternIndex == len(pattern) :
			return answerList
	else :
		patternIndex = 0
	for c in parent :
		print c.tag
		findPattern(c, pattern, patternIndex)





root = XML_read('RunXML.in', sys.stdout)
#print ElementTree.dump()

i=0
for child in root.iter():
	#print "here!"
	child.set('position', str(i))
	i=i+1

ET.dump(root)


indexedTree = indexTree(root)
#print indexedTree

print root.get("position")

searchPattern = indexTree(root[1])


print indexedTree
print searchPattern 

treeroot = root[0].tag   # THU
patternParent = searchPattern[0]
patternChild = searchPattern[1]

findPattern (root[0], searchPattern, 0)




#for country in root.findall('country'):


#print list(root)
