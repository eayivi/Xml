#
# Enam Ayivi
# aea787
# Paul Carroll
# pvc95
#


import xml.etree.ElementTree as ET
import sys


def xml_read(r, w):
	'''
	reads xml tags from file into a string returns them as an element tree
	r is a reader
	w is a writer
	raises exception if no input
	returns root of element tree
	'''
	line = r.readline()
	xml = line
	assert type(line) == str
	assert type(line) == type(xml)
	while line != '' and line != '\n':
		line = r.readline()
		xml += line
	if len(xml) == 0:
		raise EOF
		assert False

	xml = "<XML>" + xml + "</XML>" 
	assert len(xml) > 10
	assert type(xml) == str
	return ET.fromstring(xml)

def indexTree (root):
	'''
	converts element tree to a list
	root is the root of an element tree
	returns list representation of element tree
	'''
	indexedTreeHelper = [] 		# ['XML', 'THU', 'Team' ...]
	for child in root.iter():
		indexedTreeHelper.append(child.tag)
	assert type(indexedTreeHelper) == list
	return indexedTreeHelper

def validatePattern(s, t) :#parent is root of tree
	'''
	s is an element in the search pattern
	t is an element in the search tree
	return False is pattern doesn't match
	if execution completes, pattern match is validated
	'''
	matches = 0

	# check for children of search pattern element in children of search tree element
	for sc in s:			# sc is a child of the search pattern element
		for tc in t:		# tc is a child of the search tree element
			assert type(sc) == type(tc)
			if sc.tag == tc.tag:
				matches += 1
	if matches != len(s.findall('*')):
		return False
	assert matches == len(s.findall('*'))
	# recurse deeper into tree if match found
	b = True
	for sc in s:
		for tc in t:
			if sc.tag == tc.tag:
				b = validatePattern(sc, tc)
				if b == False:
					return False
	assert b != False
	
def xml_solve(r, w):
	'''
	calls read for each test case, handles validatePattern calls and return values
	r is a reader
	w is a writer
	catches exception raised by xml_read in the event of an empty test case or EOF
	'''
	while True:
		try:
			root = xml_read(r, w)

			i=0
			for child in root.iter():
				child.set('position', str(i))	# add 'position' attribute to tree elements
				i=i+1

			treeSize = 0					# number of element in search tree
			for i in root[0].iter():
				treeSize += 1

			treeroot = root[0].tag   # THU
			assert type(treeroot) == str

			# find locations of search pattern root in search tree
			potentialMatches = []
			for c in root[0].iter():
				if c.tag == root[1].tag:
					potentialMatches.append(c.get('position'))

			#print 'POTENTIAL MATCHES: ' + str(potentialMatches)

			# validate potential matches
			matchIndex = 0

			for e in root[0].iter():
				assert type(e) == type(root)
				if matchIndex < len(potentialMatches) and e.get('position') == potentialMatches[matchIndex]:
					b = validatePattern(root[1], e)
					assert b == False or b == None
					if b != False:
						assert matchIndex < len(potentialMatches)
						matchIndex += 1
					else:
						potentialMatches = potentialMatches[:matchIndex] + potentialMatches[matchIndex+1:]

			#print 'VALIDATED MATCHES: ' + str(potentialMatches)

			assert type(potentialMatches) == list

			w.write(str(len(potentialMatches)) + '\n')
			for i in potentialMatches:
				w.write(str(i) + '\n')
			w.write('\n')
		except:
			return 0

