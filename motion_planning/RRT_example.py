import matplotlib.pyplot as plt
import networkx as nx
import random

def dist(a,b):
	return sum(map(lambda x,y:(x-y)**2.0,a,b))**0.5

def rand_point(bounds):
	min_p = bounds[0]
	max_p = bounds[1]
	span = map(lambda x,y: y-x, min_p,max_p)
	p = map(lambda x,y: x+y*random.random(),min_p,span)
	return tuple(p)

def RRT(e_bounds, root, P, K, delta):
	G = nx.Graph()
	G.add_node(root)
	for i in range(0,K):
		r_points = map(lambda x: rand_point(e_bounds),range(0,P))
		to_add = []
		for p in r_points:
			if p[0] > 1.0 and p[1] > 1.0 and p[0] < 1.5 and p[1] < 1.5:
				continue
			best = min(G.nodes(),key=lambda x:dist(p,x))
			if dist(p,best)<delta:
				to_add.append((p,best))
		for pair in to_add:
			G.add_node(pair[0])
			G.add_edge(pair[0],pair[1])
	return G

G = RRT([(0,0),(2,2)], (1,1), 100, 10, .2)
locs = {}
for p in G.nodes():
	locs[p]=p
nx.draw(G,locs)
plt.show()