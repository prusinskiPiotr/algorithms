with open('data_3.txt') as file:
    V1, V2 = file.readlines()

v1, v2 = V1.rstrip().split(','), V2.rstrip().split(',')

def make_moves(vector_list):
    coords_list = [[0,0]]
    for vector in vector_list:
        x = coords_list[-1][0]
        y = coords_list[-1][1]
        direction = vector[0]
        distance = int(vector[1:])
        for i in range(1, distance+1):
            if direction == 'R':
                coords_list.append([x+i,y])
            if direction == 'U':
                coords_list.append([x,y+i])
            if direction == 'L':
                coords_list.append([x-i,y])
            if direction == 'D':
                coords_list.append([x,y-i])
    return coords_list

A, B = list(set(map(tuple, make_moves(v1)))), list(set(map(tuple, make_moves(v2))))
intersections = set(A).intersection(set(B))
sorted_distances = sorted([abs(i[0])+abs(i[1]) for i in intersections])
distance_and_coords = sorted([[abs(i[0])+abs(i[1]),f'x:{i[0]},y:{i[1]}'] for i in intersections])
print(distance_and_coords)
