import re
from collections import defaultdict

def a():
    start = list(adj)[0]
    subgraph = {start}
    out_edges = {(start, end) for end in adj[start]}
    while len(out_edges) > 3:
        next_nodes = set(edge[1] for edge in out_edges)
        next_node = min(next_nodes, key=lambda node: sum(-1 if n in subgraph else 1 for n in adj[node]))
        subgraph.add(next_node)
        for end in adj[next_node]:
            if end in subgraph:
                out_edges.remove((end, next_node))
            else:
                out_edges.add((next_node, end))
    
    return len(subgraph) * (len(adj) - len(subgraph))
            
if __name__ == '__main__':
    adj = defaultdict(list)
    with open('input.txt', 'r') as f:
        l = f.readline().strip()
        while l:
            l = re.split(r': | ', l)
            for c in l[1:]:
                adj[l[0]].append(c)
                adj[c].append(l[0])
            l = f.readline().strip()
    
    print(a())