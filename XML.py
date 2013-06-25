#
# Enam Ayivi
# aea787
# Paul Carroll
# pvc95
#


import xml.etree.ElementTree as ET
import sys


def xml_read(r, w):

	line = r.readline()
	xml = line

	while line != "":
		line = r.readline()
		xml += line
	
	xml = "<XML>" + xml + "</XML>" 
	
	return ET.fromstring(xml)

def indexTree (root):
	indexedTreeHelper = [] 		# ['XML', 'THU', 'Team' ...]
	for child in root.iter():
		indexedTreeHelper.append(child.tag)
	return indexedTreeHelper

'''
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
'''

def validatePattern(s, t) :#parent is root of tree
	'''
	sp is an element in the search pattern
	t is an element in the search tree
	return False is pattern doesn't match
	if execution completes, pattern match is validated
	'''
	print 'validatePattern'
	matches = 0

	print s,
	print t

	for sc in s:
		for tc in t:
			print sc,
			print tc
			if sc == tc:
				matches += 1
	#if matches != len(s.findall('*')):
		#return False
	#print matches,
	#print len(s.findall('*'))
	#print s.findall('*')



def xml_solve(r, w):
	root = xml_read(sys.stdin, sys.stdout)
	
	i=0
	for child in root.iter():
		child.set('position', str(i))	# add 'position' attribute to tree elements
		i=i+1

	indexedTree = indexTree(root[0])	# search tree as list

	treeSize = 0					# number of element in search tree
	for i in root[0].iter():
		treeSize += 1
	
	searchPattern = indexTree(root[1])	# search pattern as list

	treeroot = root[0].tag   # THU

	

	# find locations of search pattern root in search tree
	potentialMatches = []
	for c in root[0].iter():
		if c.tag == root[1].tag:
			potentialMatches.append(c.get('position'))

	#print potentialMatches

	# validate potential matches

	matchIndex = 0



	for e in root[0].iter():
		b = True
		if matchIndex < len(potentialMatches) and e.get('position') == potentialMatches[matchIndex]:
			b = validatePattern(root[1], e)
			matchIndex += 1
		if b == False:
			potentialMatches.remove(potentialMatches[matchIndex])
			matchIndex -= 1
		

	#print potentialMatches



	#l = findPattern (root[0], searchPattern, 0, 0, [], treeSize)	# 

	#print l

