barang = input("Masukkan barang apa saja yang ingin dibeli(pisahkan dengan koma): ")

splitbarang = barang.split(",")
total_barang = len(splitbarang)
total_diskon = 0
jumlah_harga = 0

for b in range (total_barang):
    harga = int(input("Berapa harga barang "+splitbarang[b]+ " ?:"))
    jumlah_harga += harga

    if harga >= 100000 and harga < 250000:
        diskon = harga*0.10
        total_diskon += diskon
        print("Harga", splitbarang[b],"\t Rp.",harga,"\t","Diskon Rp.",diskon)
    elif harga >= 250000:
        diskon = harga*0.25
        total_diskon += diskon
        print("Harga", splitbarang[b],"\t Rp.",harga,"\t","Diskon Rp.",diskon)
    else:
        print("Harga", splitbarang[b],"\t Rp.",harga,"\t","Diskon Rp.",0)

total_uang = jumlah_harga - total_diskon

print("Total diskon yang anda dapatkan adalah sebesar: Rp.", total_diskon)
print("Total uang yang harus anda bayarkan adalah: Rp.",total_uang)