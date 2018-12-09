with open('diagram_walls.txt') as f:
    read_data = f.read()

count = 0
w = 30
h = 15
x_pos_matrix = [[y for x in range(w)] for y in range(h)]
y_pos_matrix = [[x for x in range(h)] for y in range(w)]
print(x_pos_matrix)
zipped_list = zip(x_pos_matrix, y_pos_matrix)
zipped_list = list(zipped_list)
# print(zipped_list)

def counter():
    for i in range(15):
        count = 0
        print(i)
        while count < 30:
            print(count)
            print(read_data[count])
            if read_data[count] == '#':
                matrix[i][count] = count
            count = count + 1
    # print(matrix)

