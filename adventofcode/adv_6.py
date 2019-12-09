from collections import defaultdict

with open('data_6.txt') as file:
    data = file.readlines()

a = [data[i].rstrip().split(')') for i, num in enumerate(data)]

def DFS(G,v,seen=None,path=None):
    if seen is None: seen = []
    if path is None: path = [v]

    seen.append(v)

    paths = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(list(t_path))
            paths.extend(DFS(G, t, seen[:], t_path))
    return paths

G = defaultdict(list)
for (s,t) in a:
    G[s].append(t)

all_paths = DFS(G, 'COM')
orbits_sum = sum(len(i)-1 for i in all_paths)
print(orbits_sum)
