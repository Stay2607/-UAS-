def cekPassword(pas):
    kapital = 0
    angka = 0
    if len(pas) >= 6 and len(pas) <= 15:
        for i in pas:
            if i.isupper():
                kapital += 1
        for j in pas:
            if j.isdigit():
                angka += 1
        if angka == 0 and kapital == 0:
            return "Password harus mengandung minimal 1 digit angka dan 1 huruf kapital"
        elif angka == 0:
            return "Password harus mengandung minimal 1 digit angka"
        elif kapital == 0:
            return "Password harus mengandung minimal 1 huruf kapital"
        else:
            return "password valid! Random Password: {}{}{}".format(angka, kapital, pas)
    else:
        return "Panjang password harus 6-15 karakter"


print(cekPassword("admin"))
print(cekPassword("reload"))
print(cekPassword("powerOff"))
print(cekPassword("cloud24"))
print(cekPassword("Cinema21"))
print(cekPassword("CafeOutDOOR7890"))
