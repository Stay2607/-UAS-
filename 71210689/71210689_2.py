def cekPassword(x):
    kap = 0
    for i in list(x):
        if i.isupper():
            kap += 1
        else:
            kap += 0
    angka = 0
    aa = "1234567890"
    a = list(aa)
    for i in list(x):
        if i in a:
            angka += 1
        else:
            angka = +0
    if len(x) < 6 or len(x) > 15:
        return "Panjang password harus 6-15 karakter"
    elif kap == 0 and angka == 0:
        return "Password harus mengandung minimal 1 digit angka dan 1 huruf kapital"
    elif kap == 0:
        return "Password harus mengandung minimal 1 huruf kapital"
    elif angka == 0:
        return "Password harus mengandung minimal 1 digit angka"
    else:
        rndm = "{}{}{}".format(angka, kap, x)
        a = "Password valid! Random password: {}".format(rndm)
        return a


print(cekPassword("admin"))
print(cekPassword("reload"))
print(cekPassword("powerOff"))
print(cekPassword("cloud24"))
print(cekPassword("Cinema21"))
print(cekPassword("CafeOutDOOR7890"))
