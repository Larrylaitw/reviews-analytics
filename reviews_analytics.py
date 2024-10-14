data = []
count = 0
with open('test.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 2 == 0:
            print(len(data))
print(len(data))
print(data[21])