import random

fw = open('accTestGen.out', 'w')

for i in range(100):		# number of test cases
	numTags = int(random.random() * 100 + 1)
	numTags2 = int(random.random() * 10 + 1)

	if numTags2 > numTags:
		numTags, numTags2 = numTags2, numTags

	# search tree
	l = []

	for j in range(numTags):
		tag = chr(int(random.random() * 26 + 65))
		l.append(tag)

	for t in l:
		fw.write('<' + t + '>\n')
	for t in reversed(l):
		fw.write('</' + t + '>\n')

	# search pattern
	l2 = []

	for j in range(numTags2):
		tag = chr(int(random.random() * 26 + 65))
		l2.append(tag)

	for t in l2:
		fw.write('<' + t + '>\n')
	for t in reversed(l2):
		fw.write('</' + t + '>\n')
	fw.write('\n')
