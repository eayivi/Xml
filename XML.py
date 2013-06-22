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

def findPattern(parent, pattern, patternIndex, treeIndex, patternLocations, treeSize) :#parent is root of tree
	if parent.tag == pattern[patternIndex] :		#patternIndex is how deep we are in the pattern sought
		if patternIndex == 0:
			treeIndex = parent.get('position')
		patternIndex += 1
		if patternIndex == len(pattern) :			# found all elements from search pattern
			patternLocations.append(treeIndex)							# list of locations of pattern
			patternIndex = 0
	else :
		patternIndex = 0
	if int(parent.get('position')) == treeSize:
		return patternLocations

	for c in parent :
		ret = findPattern(c, pattern, patternIndex, treeIndex, patternLocations, treeSize)
		if type(ret) is list:
			return patternLocations




root = XML_read('RunXML.in', sys.stdout)
#print ElementTree.dump()

i=0
for child in root.iter():
	child.set('position', str(i))
	i=i+1

ET.dump(root)


indexedTree = indexTree(root[0])
#print indexedTree

treeSize = 0
for i in root[0].iter():
	treeSize += 1

searchPattern = indexTree(root[1])



treeroot = root[0].tag   # THU
patternParent = searchPattern[0]
patternChild = searchPattern[1]

l = findPattern (root[0], searchPattern, 0, 0, [], treeSize)

print l


#for country in root.findall('country'):


#print list(root)
