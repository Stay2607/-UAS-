# Program 3
# Maaf tidak sesuai dengan test cast nya, tapi hanya ini yang saya bisa
# Terima kasih
nama_barang1 = str(input("Nama barang 1: "))
harga_barang1 = int(input("harga barang 1: Rp "))
nama_barang2 = str(input("Nama barang 2: "))
harga_barang2 = int(input("harga barang 2: Rp "))
# jumlah yang harus dibayar adalah berapa total belanjaannya
# tapi kalau dapat diskon akan berkurang
total_harga = harga_barang1 + harga_barang2

# jika dia belanja di atas 100rb maka berikan bonus dan diskon


if total_harga >= 250000:
    diskon = (total_harga) * (25 / 100)
    bayar = total_harga - diskon
    print("Berapa harga barang 1 Rp. ", total_harga)
    print("Total diskon Rp. ", diskon)
elif total_harga >= 100000:
    diskon = (total_harga) * (10 / 100)
    bayar = total_harga - diskon
    print("Berapa harga barang 1 Rp. ", total_harga)
    print("Total diskon Rp. ", diskon)
