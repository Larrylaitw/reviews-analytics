data = []
count = 0
with open('test.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 2 == 0:
            print(len(data))
print('第一筆為', data[0])
print('總共資料為', len(data), '筆')