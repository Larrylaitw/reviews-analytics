data = []
count = 0
a = 0
with open('test.txt', 'r') as f:
    for line in f:
        a = len(line) + a
        data.append(line.strip())
        count += 1  #可以顯示讀取狀態
        if count % 1 == 0:
            print(len(data))
print('文章字數統計功能, 離開請按 q')
print('總共資料為', len(data), '筆')
print('總共用了', a, '字元')

t = [] #用關鍵字找文字
for d in data:
    if 'work' in d:
        t.append(d.strip())
print(t)

#統計重複的字
wc = {}
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word]= 1 #新增key到wc字典裡

for word in wc:
    print(word, ':', wc[word])

while True:
    word = input('請輸入你要搜尋的字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '共出現了', wc[word], '次')
    else:
        print('沒有這個字')
print('感謝 and 慢走')




