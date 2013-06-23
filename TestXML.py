#!/usr/bin/env python


"""
To test the program:
    % python TestCollatz.py >& TestCollatz.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest
import xml.etree.ElementTree as ET

from XML import xml_read, indexTree, findPattern, xml_solve

# -----------
# TestCollatz
# -----------

class TestXML (unittest.TestCase) :
	# ----
	# read
	# ----

	def test_read_1 (self) :
		r = StringIO.StringIO("<a></a>\n<a></a>")
		w = StringIO.StringIO()
		b = xml_read(r, w)
		self.assert_(b.tag == 'XML')
		self.assert_(b[0].tag ==  'a')
		self.assert_(b[1].tag == 'a')

	def test_read_2 (self) :
		r = StringIO.StringIO("<a><b></b></a>\n<a></a>")
		w = StringIO.StringIO()
		b = xml_read(r, w)
		self.assert_(b.tag == 'XML')
		self.assert_(b[0][0].tag ==  'b')
		self.assert_(b[1].tag == 'a')

	def test_read_3 (self) :
		r = StringIO.StringIO("<a><b></b><c></c><d></d></a>\n<a><b><c></c></b></a>")
		w = StringIO.StringIO()
		b = xml_read(r, w)
		self.assert_(b.tag == 'XML')
		self.assert_(b[0].tag ==  'a')
		self.assert_(b[0][0].tag ==  'b')
		self.assert_(b[0][1].tag ==  'c')
		self.assert_(b[0][2].tag ==  'd')
		self.assert_(b[1].tag ==  'a')
		self.assert_(b[1][0].tag ==  'b')
		self.assert_(b[1][0][0].tag ==  'c')


	# ---------
	# indexTree
	# ---------

	def test_indexTree_1 (self) :
		l = indexTree(ET.fromstring("<a></a>"))
		self.assert_(len(l) == 1)
		self.assert_(l == ['a'])

	def test_indexTree_2 (self) :
		l = indexTree(ET.fromstring("<a><b></b></a>"))
		self.assert_(len(l) == 2)
		self.assert_(l == ['a', 'b'])

	def test_indexTree_3 (self) :
		l = indexTree(ET.fromstring("<a><b><c><d></d><e></e></c></b></a>"))
		self.assert_(len(l) == 5)
		self.assert_(l == ['a', 'b', 'c', 'd', 'e'])
	# -----------
	# findPattern
	# -----------

	def test_findPattern_1 (self) :
		r = StringIO.StringIO("<a></a>\n<a></a>")
		w = StringIO.StringIO()
		root = xml_read(r, w)
		pat = indexTree(root[1])
		i=0
		for child in root.iter():
			child.set('position', str(i))
			i=i+1
		treeSize = 0
		for i in root[0].iter():
			treeSize += 1
		l = findPattern(root[0], pat, 0, 0, [], treeSize)
		self.assert_(l == ['1'])

	def test_findPattern_1 (self) :
		r = StringIO.StringIO("<a></a>\n<b></b>")
		w = StringIO.StringIO()
		root = xml_read(r, w)
		pat = indexTree(root[1])
		i=0
		for child in root.iter():
			child.set('position', str(i))
			i=i+1
		treeSize = 0
		for i in root[0].iter():
			treeSize += 1
		l = findPattern(root[0], pat, 0, 0, [], treeSize)
		self.assert_(l == [])

	def test_findPattern_1 (self) :
		r = StringIO.StringIO("<a><b><a></a></b></a>\n<a></a>")
		w = StringIO.StringIO()
		root = xml_read(r, w)
		pat = indexTree(root[1])
		i=0
		for child in root.iter():
			child.set('position', str(i))
			i=i+1
		treeSize = 0
		for i in root[0].iter():
			treeSize += 1
		l = findPattern(root[0], pat, 0, 0, [], treeSize)
		self.assert_(l == ['1', '3'])

	# -----
	# solve
	# -----

	def test_solve_1 (self) :
		r = StringIO.StringIO("<a><b></b></a>\n<a><b></b></a>")
		w = StringIO.StringIO()
		#xml_solve(r, w)
		self.assert_(w.getvalue() == "")



'''
	# -----
	# print
	# -----

	def test_print_1 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 1, 10, 20)
		self.assert_(w.getvalue() == "1 10 20\n")

	def test_print_2 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 100, 200, 125)
		self.assert_(w.getvalue() == "100 200 125\n")

	def test_print_3 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 900, 1000, 174)
		self.assert_(w.getvalue() == "900 1000 174\n")


'''

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
