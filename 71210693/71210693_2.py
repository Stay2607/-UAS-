def cekPassword(pw):
    print()
    banyak_angka = sum(1 for c in pw if c.isdigit())
    banyak_kapital = sum(1 for c in pw if c.isupper())

    if len(pw) < 6 or len(pw) > 15:
        return "Panjang password harus 6-15 karakter"
    elif banyak_kapital < 1 and banyak_angka < 1:
        return "Password harus mengandung minimal 1 digit angka dan 1 huruf kapital"
    elif banyak_kapital < 1:
        return "Password harus mengandung minimal 1 huruf kapital"
    elif banyak_angka < 1:
        return "Password harus mengandung minimal 1 digit angka"
    else:
        return (
            "Password Valid! Random Password:"
            + str(banyak_angka)
            + str(banyak_kapital)
            + pw
        )


print(cekPassword("admin"))
print(cekPassword("reload"))
print(cekPassword("powerOff"))
print(cekPassword("cloud24"))
print(cekPassword("Cinema21"))
print(cekPassword("CafeOutDOOR7890"))
