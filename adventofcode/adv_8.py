with open('data_8.txt') as file:
    data = file.read()

a = [data[i:i+150] for i in range(0, len(data), 150)]
zeros_dict = {i:a[i].count('0') for i in range(0, len(a))}
least_zeros_index = min(zeros_dict, key=zeros_dict.get)
result = a[least_zeros_index].count('1') * a[least_zeros_index].count('2')
print(result)
