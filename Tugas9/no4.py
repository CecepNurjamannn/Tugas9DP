number = [105, 20, 8, 150, 30, 5, 200]

hasil = []
for i in number:
    if 10 <= i <= 100:
        hasil.append(i)

hasil.sort()
print(hasil)
