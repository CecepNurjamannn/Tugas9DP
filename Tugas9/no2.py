number = [7, 4, 9, 2, 5, 1]

hasil = []
for i in number:
    if i % 2 == 0:
        hasil.append(i)

hasil.sort()
print(hasil)
