def cekPassword(pwd):
    print("")
    HurufBesar = 0
    Angka = 0
    if len(pwd) <= 15 and len(pwd) >= 6:
        for char in pwd:
            if char.isupper():
                HurufBesar += 1
            if char.isdigit():
                Angka += 1
        if HurufBesar == 0 and Angka == 0:
            return "Password harus mengandung minimal 1 digit angka dan 1 huruf kapital"
        elif Angka == 0:
            return "Password harus mengandung minimal 1 digit angka"
        elif HurufBesar == 0:
            return "Password harus mengandung minimal 1 huruf kapital"
        else:
            return "Password valid! Random Password: {}{}{}".format(str(Angka), str(HurufBesar), str(pwd))
    else:
        return "Panjang password harus 6-10 karakter"


print(cekPassword("admin"))
print(cekPassword("reload"))
print(cekPassword("powerOff"))
print(cekPassword("cloud24"))
print(cekPassword("Cinema21"))
print(cekPassword("CafeOutDOOR7890"))
