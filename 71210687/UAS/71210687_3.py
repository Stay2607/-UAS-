barang = input("Masukkan barang apa saja yang ingin dibeli(pisahkan dengan koma): ")
koma = barang.split(",")
harga = len(koma)

Discount = 0
Sum = 0
for i in range(harga):
    Price = "Berapa harga barang " + koma[i] + " ?:"
    ItemPrice = input(Price)
    Sum += int(ItemPrice)
    if int(ItemPrice) >= 250000:
        Dsc = float(float(ItemPrice) * 0.25)
        Discount += Dsc
        print("Harga {} \t Rp.  {} \t Diskon Rp.  {}".format(koma[i], ItemPrice, Dsc))
    elif int(ItemPrice) < 100000:
        print(
            "Harga {}".format(koma[i]),
            "\t Rp.  {}".format(ItemPrice),
            "\t",
            "Diskon Rp. ",
            0,
        )
    else:
        Dsc = float(float(ItemPrice) * 0.1)
        Discount += Dsc
        print("Harga {} \t Rp.  {} \t Diskon Rp.  {}".format(koma[i], ItemPrice, Dsc))
Total = Sum - Discount
print("Total diskon yang anda dapatkan adalah sebesar: Rp. ", Discount)
print("Total uang yang harus anda bayarkan adalah: Rp. ", Total)
