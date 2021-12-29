item = input("Masukkan barang apa saja yang ingin dibeli (pisahkan dengan koma) : ")
list = item.split(",")
totbarang = len(list)
diskon = 0
tot = 0
for i in range(totbarang):
    harga = "Berapa harga barang" + list[i] + "?:"
    barang = input(harga)
    tot = tot + int(barang)
    if int(barang) < 100000:
        print("Harga" + list[i] + "\t Rp. " + barang + "\t Diskon Rp. ", 0)
    elif int(barang) >= 100000 and int(barang) < 250000:
        potong = float(float(barang) * 0.1)
        diskon = diskon + potong
        print("Harga" + list[i] + "\t Rp. " + barang + "\t Diskon Rp. ", potong)
    elif int(barang) >= 250000:
        potong = float(float(barang) * 0.25)
        diskon = diskon + potong
        print("Harga" + list[i] + "\t Rp. " + barang + "\t Diskon Rp. ", potong)
jumlah = tot - diskon
print("Total diskon yang anda dapatkan adalah sebesar: Rp. ", diskon)
print("Total uang yang harus anda bayarkan adalah: Rp. ", jumlah)
print()
