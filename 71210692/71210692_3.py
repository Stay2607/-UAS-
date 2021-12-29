barang = list(input("Masukkan barang apa saja yang ingin dibeli (pisahkan dengan koma) : ").split(","))

print(len(barang))
ht = []
dt = []
ur = 0

for i in barang:
    print("Berapa harga barang", barang[ur], "?", end="")
    harga = int(input(" "))
    if int(harga) >= 250000:
        diskon = harga * (25 / 100)
    elif int(harga) >= 100000:
        diskon = harga * (10 / 100)
    else:
        diskon = 0
    ht.append(harga)
    dt.append(diskon)

    print("Harga", barang[ur], end="")
    print(" Rp.", harga, end="")
    print(" Diskon Rp.", diskon)

    ur += 1

da = sum(dt)
akhir = sum(ht) - da
print("Total diskon yang anda dapatkan adalah sebesar: Rp.", da)
print("Total uang yang harus anda bayarkan adalah: Rp.", akhir)
