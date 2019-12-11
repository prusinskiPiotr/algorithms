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
    G[t].append(s)

longest_depth_paths = DFS(G, 'COM')
orbits_sum = sum(len(i)-1 for i in longest_depth_paths)
# print(orbits_sum)
all_paths = [p for ps in [DFS(G, n) for n in set(G)] for p in ps]
san = [i for i in all_paths if ('YOU' in i) and ('SAN' in i)]
print(len(san[0])-3)

# this code is terribly inefficient and takes forever to execute
# but it gets the result.