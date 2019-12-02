with open('data_1.txt') as file:
    data = file.read()
print(sum(((int(i)//3)-2) for i in data.splitlines()))
total_fuel = 0
for i in data.splitlines():
    temp = ((int(i)//3)-2)
    total_fuel += temp
    while temp > 0:
        temp = (temp//3)-2
        if temp > 0:
            total_fuel += temp
print(total_fuel)
