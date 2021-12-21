barangyangdibeli = input(
    "Masukkan barang apa saja yang ingin dibeli(pisahkan dengan koma): "
)
list = barangyangdibeli.split(",")
banyakbarang = len(list)
jmlh = 0
totaldis = 0
for x in range(banyakbarang):
    harga = "Berapa harga barang " + list[x] + " ?:"
    barangyangdibeli = input(harga)
    jmlh += int(barangyangdibeli)
    if int(barangyangdibeli) >= 250000:
        dis = float(float(barangyangdibeli) * 0.25)
        totaldis += dis
        print(
            ("Harga {}\t Rp. {}\t Diskon Rp. {}").format(list[x], barangyangdibeli, dis)
        )
    elif int(barangyangdibeli) >= 100000 and int(barangyangdibeli) < 250000:
        dis = float(float(barangyangdibeli) * 0.1)
        totaldis += dis
        print(
            ("Harga {} \t Rp. {}\t Diskon Rp. {}").format(
                list[x], barangyangdibeli, dis
            )
        )
    else:
        print(
            ("Harga {}\t Rp. {}\t Diskon Rp. {}").format(list[x], barangyangdibeli, 0)
        )
jumlahtotal = jmlh - totaldis
print("Total diskon yang anda dapatkan adalah sebesar: Rp. ", totaldis)
print("Total uang yang harus anda bayarkan adalah: Rp. ", jumlahtotal)
