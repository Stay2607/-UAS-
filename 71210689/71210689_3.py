aa = input("Masukkan barang apa saja yang ingin dibeli (pisahkan dengan koma): ")
a = aa.split(",")
c = 0
b = 0
for i in a:
    harga = int(input("Berapa harga barang " + i + "?: "))
    if harga >= 100000 and harga < 250000:
        diskon = 10 / 100 * harga
    elif harga >= 250000:
        diskon = 25 / 100 * harga
    else:
        diskon = 0
    print("Harga " + i + " " + " Rp. " + str(harga) + " diskon Rp. " + str(diskon))

    c += diskon

    b += harga

print("Total diskon yang harus anda dapatkan adalah sebesar:", c)
print("Total uang yang harus anda bayarkan adalah:", b - c)
