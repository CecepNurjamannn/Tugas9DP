kata = ["apel","jeruk","mangga","pisang","anggur","durian"]

hasil = []
for i in kata:
    if len(i) >= 5 :
        hasil.append(i)

hasil.sort()
print(hasil)
