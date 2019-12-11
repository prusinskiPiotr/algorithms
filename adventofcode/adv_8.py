with open('data_8.txt') as file:
    data = file.read()

layers = [data[i:i+150] for i in range(0, len(data), 150)]
zeros_dict = {i:layers[i].count('0') for i in range(0, len(layers))}
least_zeros_index = min(zeros_dict, key=zeros_dict.get)
result = layers[least_zeros_index].count('1') * layers[least_zeros_index].count('2')
print(result)

layered_image = []
for i in range(0, 150):
    for j in layers:
        if j[i] == '0' or j[i] == '1':
            layered_image.append(j[i])
            break

unsplit_final = ''.join(layered_image)
decoded_image = [unsplit_final[i:i+25] for i in range(0, len(unsplit_final), 25)]
for i in decoded_image:
    print(i)
