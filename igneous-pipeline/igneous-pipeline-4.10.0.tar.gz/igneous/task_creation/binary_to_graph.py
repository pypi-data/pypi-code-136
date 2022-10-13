import numpy as np
from cloudvolume import Skeleton

def neighborhood(x,y,z,sx,sy,sz):
	n26 = []
	for dx in range(-1,2):
		for dy in range(-1,2):
			for dz in range(-1,2):
				if dx == dy and dy == dz and dz == 0:
					continue
				if not (x+dx >= 0 and x+dx < sx and y+dy >= 0 and y+dy < sy and z+dz >= 0 and z+dz < sz):
					continue
				n26.append((x+dx, y+dy, z+dz))
	return n26

def extract_graph(binimg):
	sx,sy,sz = binimg.shape
	edges = set()
	for x in range(sx):
		for y in range(sy):
			for z in range(sz):
				if binimg[x,y,z] == 0:
					continue

				for nx,ny,nz in neighborhood(x,y,z,sx,sy,sz):
					if binimg[nx,ny,nz] == 0:
						continue

					if (x+sx*(y+sy*z)) < (nx+sx*(ny+sy*nz)):
						edges.add(((x,y,z), (nx,ny,nz)))
					else:
						edges.add(((nx,ny,nz), (x,y,z)))

	return edges

def graph_to_skel(edges):
	numbering = {}

	i = 0
	for edge in edges:
		for v in edge:
			if v not in numbering:
				numbering[v] = i
				i += 1

	inumbering = {v,k for k,v in numbering.items()}
	vertices = []
	for i in range(len(inumbering)):
		vertices.append(inumbering[i])

	int_edges = []
	for v1,v2 in edges:
		int_edges.append((numbering[v1], numbering[v2]))

	return Skeleton(vertices, int_edges)




