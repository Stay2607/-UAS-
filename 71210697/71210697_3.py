barang = (
    int,
    input("Masukan barang apa saja yang ingin dibeli (pisahkan dengan koma) :"),
)
barang1 = int(input("Berapa harga barang H&M ? :"))
x = barang1 * 25 // 100
x1 = barang1 - x
print("Harga H&M         Rp.", barang1, "Diskon Rp.", x)
barang2 = int(input("Berapa harga barang Nike X Dior ? :"))
y = barang2 * 25 // 100
y1 = barang2 - y
print("Harga Nike X Dior     Rp.", barang2, "Diskon Rp.", y)
barang3 = int(input("Berapa harga Gucci Horsebit ? :"))
z = barang3 * 10 // 100
z1 = barang3 - z
print("Harga Gucci Horsebit    Rp.", barang3, "Diskon Rp.", z)
barang4 = int(input("Berapa harga barang besace tplyo ? :"))
print("Harga barang besace tokyo Rp. ", barang4, "Diskon 0")
barang5 = int(input("Berapa harga barang royal kludge ?:"))
print("Harga royal kludge    Rp.", barang5, "Diskon 24999")
total = x1 + y1 + z1 + barang4 + barang5
print("Total Diskon yang anda dapatkan adalah sebesarRp. :", total)
print("Total uang yang harus anda bayarkan adalah Rp.:", total)
