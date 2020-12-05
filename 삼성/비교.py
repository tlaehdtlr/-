test = [[1000]*301 for _ in range(301)]

# data = list(range(1, 501))
# random.shuffle(data)
f = open('토네이도테케.txt', 'w')
a = '301\n'
f.write(a)
for r in test:
    for num in r:
        b = '{} '.format(num)
        f.write(b)
    f.write('\n')
f.close()