inp1 = int(input("Masukkan angka pertama: "))
inp2 = int(input("Masukkan angka kedua: "))

if inp1 % 2 == 0 and inp2 % 2 == 0:
    hitung = inp1 ** inp2
    print("Hasil yang didapat adalah {}\n".format(hitung))
if inp1 % 2 == 1 and inp2 % 2 == 0:
    hitung = inp1 / inp2
    print("Hasil yang didapat adalah {}\n".format(hitung))
if inp1 % 2 == 0 and inp2 % 2 == 1:
    hitung = inp1 + inp2
    print("Hasil yang didapat adalah {}\n".format(hitung))
if inp1 % 2 == 1 and inp2 % 2 == 1:
    hitung = inp1 - inp2
    print("Hasil yang didapat adalah {}\n".format(hitung))
