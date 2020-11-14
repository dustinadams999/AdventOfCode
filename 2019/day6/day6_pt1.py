import sys

def main(filename):
	# build the graph
	# com will point at the root
	f = open(filename, 'r')
	first = True
	graph = {}
	for i in f.readlines():
		parent = i.split(')')[0]
		child = i.split(')')[1]
		if first:
			graph[parent] = [child]
			first = False
		# find the parent node
		else:
			parent_node = find_parent(graph, parent)
			graph[parent_node].append(child)
	#com = None

	total = count(graph['com'], 0)

def find_parent(graph, parent):
	# find and return the parent
	target = None
	# TODO: FIND THE TARGET NODE
	return target

def count(N, level):
	if N.keys() == None:
		return level
	else:
		total = 0
		for k in N.keys():
			total += level + count(c, level + 1)
		return total

if __name__ == '__main__':
	filename = sys.argv[1]
	main(filename)
