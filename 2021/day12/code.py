import numpy as np

#### Read Data from txt file
#### and put in list named Data

file = open('data.txt', 'r')
raw_text = file.readlines()

### Inspired by Spirited-Airline4702 from Reddit
### Lower case nodes once and upper case infinite

n = len(raw_text)
edge_start = []
edge_end = []
for i in range(n):
    x = raw_text[i].split('-')
    edge_start.append(x[0])
    edge_end.append(x[1].split()[0])

nodes = list(set(edge_start) | set(edge_end))
m = len(nodes)

g = {i: [] for i in nodes}

for i in range(m):
    for j in range(n):
        if nodes[i] == edge_start[j]:
            g[nodes[i]].append(edge_end[j])
        if nodes[i] == edge_end[j]:
            g[nodes[i]].append(edge_start[j])
        
def node_allowed(graph, path, node):
    if node not in g[path[-1]]:
        return False
    if node.islower() and path.count(node) == 1:
        return False
    return True

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node_allowed(graph, path, node):
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths 

print('Answer for Day 12 Part 1 is:', len(find_all_paths(g, 'start', 'end')))

### One lower case twice, other lower case once and upper case infinite

def node_allowed(graph, path, node):
    if node not in g[path[-1]]:
        return False
    if node == 'start':
        return False
    if node.islower() and path.count(node) == 2:
        return False
    if node.islower() and path.count(node) == 1:
        twice = 0
        for node in nodes:
            if node.islower() and path.count(node) == 2:
                twice = 1
        if twice == 1:
            return False
            
    return True

print('Answer for Day 12 Part 2 is:', len(find_all_paths(g, 'start', 'end')))   