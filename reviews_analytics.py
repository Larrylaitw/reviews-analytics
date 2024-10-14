data = []
count = 0
a = 0
with open('test.txt', 'r') as f:
    for line in f:
        a = len(line) + a
        data.append(line)
        #count += 1  #可以顯示讀取狀態
        #if count % 5 == 0:
            #print(len(data))
print('第一筆為', data[0])
print('總共資料為', len(data), '筆')
print('總共用了', a, '字元')
print('平均data長度為', a / len(data))

new = []
for d in data:
    if len(d) > 3:
        new.append(d)
print('總共有', len(new), '大於3個字元')