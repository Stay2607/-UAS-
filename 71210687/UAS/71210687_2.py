def cekPassword(Password):
    print()
    a = 0
    b = 0
    if len(Password) >= 6 and len(Password) <= 15:
        c = str(a)
        d = str(b)
        for char in Password:
            if char.isdigit():
                a += 1
            elif char.isupper():
                b += 1
        if a == 0:
            return "Password harus mengandung minimal 1 digit angka"
        elif b == 0:
            return "Password harus mengandung minimal 1 huruf kapital"
        elif a == 0 and b == 0:
            return "Password harus mengandung minimal 1 digit angka dan 1 huruf kapital"
        else:
            return "Password valid! Random Password: " + c + d + Password
    else:
        return "Panjang password harus 6-10 karakter"


print(cekPassword("admin"))
print(cekPassword("reload"))
print(cekPassword("powerOff"))
print(cekPassword("cloud24"))
print(cekPassword("Cinema21"))
print(cekPassword("CafeOutDOOR7890"))
