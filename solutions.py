# from itertools import permutations

# # question 1
# def question1(s, t):
#     if not s or not t or type(s) is not str or type(t) is not str or len(t) > len(s):
#         return False
#     s = s.lower()
#     t = t.lower()
#     t = [''.join(p) for p in permutations(t)]
#     print t
#     for i in t:
#         if i in s:
#             return True
#     return False

# print question1('udacity', 'aud'), "\n"
# # should return TRUE

# print question1(0,0), "\n"
# # should return FALSE

# print question1(" "," "), "\n"
# # should return TRUE

# print question1("OnBelayClimbOn", "BelayOnClimbing"), "\n"
# # should return FALSE
        
# # question 2
# def isPalindrome(s):
# 	s = s.lower()
# 	return s[::-1] == s

# def question2(s):
# 	if s != None and type(s) is str:

# 		l = ""

# 		for count, item in enumerate(s):
# 			for index, item in enumerate(s):
# 				c = s[count:index + 1]

# 				if isPalindrome(c) and len(c) > len(l):
# 					l = c

# 		return l.lower()
# 	return False


# print question2('racecar'), "\n"
# # Should return 'racecar'

# print question2('SAMMY'), "\n"
# # Should return 'mm'

# print question2(3,3,'hey'), "\n"
# # Should return False

def question3(adjDict):
	edgeList = []
	seen = []

	for vertex in adjDict.iterkeys():
		print 'VERTEX ', vertex

		# set first edge as min and compare
		minEdge = adjDict[vertex][0]
		print 'Min Edge ', minEdge

		for edge in adjDict[vertex]:
			print 'EDGE ', edge

			if edge[0] in seen:
				print 'backtrack ', edge[0]
				add = list(edge)
				add.pop(0)
				add.insert(0, vertex)
				add = tuple(add)

				pin = seen.index(edge[0])
				pin = seen[pin]
				print 'pin ', pin
				print 'ADDDDD ', add
				print 'is it in? ', adjDict[pin]

				if add in adjDict[pin]:
					print 'add is already in, skipping... may be adding to edge list'
					if edge not in edgeList:
						print 'not in edgelist, adding...'
						edgeList.append(edge)

				else:
					print 'AFTER ADD VERTEX ', adjDict[pin]
					print add, ' is not in the list!'
					adjDict[pin].append(add)

			if edge[1] < minEdge[1] and edge[1] != minEdge[1]:
				print 'adding min edge>'
				minEdge = edge

		if minEdge not in edgeList:
			edgeList.append(minEdge)

		print "edgeList = ", edgeList

		adjDict[vertex] = edgeList

		print "Vertex List = ", adjDict[vertex]

		edgeList = []
		minEdge = ('', 0)
		seen.append(vertex)


	print "Dict Done = "
	return adjDict


a = {
	'A': [('B', 3), ('D', 4)],
	'B': [('A', 3), ('E', 4), ('F', 6)],
	'C': [('E', 5)],
	'D': [('A', 4)],
	'E': [('B', 4), ('C', 5), ('F', 5)],
	'F': [('B', 6), ('E', 5)]
}

print question3(a)
# Should return
# { 
#   'A': [('B', 3), ('D', 4)],
#	'B': [('A', 3), ('E', 4)],
#	'C': [('E', 5)],
#	'D': [('A', 4)],
#	'E': [('B', 4), ('C', 5), ('F', 5)],
#	'F': [('E', 5)]
# }


