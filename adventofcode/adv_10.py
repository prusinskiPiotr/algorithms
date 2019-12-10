with open('data_10.txt') as file:
    data = file.readlines()

# x and y are inverted, meaning first bracket is y, second is x
asteroid_map = [i.rstrip().split() for i in data]
print(asteroid_map)
