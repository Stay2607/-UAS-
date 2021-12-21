kalimat="Password harus mengandung minimal "
valid="Password valid! Random Password: "

def cekPassword(pw):
    if len(pw)<6 or len(pw)>15:
        return "Panjang password harus 6-15 karakter"
    elif len(pw)>=6 and len(pw)<=15:
        kapital=0
        angka=0
        for i in pw:
            if i.isupper():
                kapital=kapital+1
            if i.isdigit():
                angka=angka+1
        if angka==0 and kapital==0:
            return kalimat+"1 digit angka dan 1 huruf kapital"
        elif kapital==0:
            return kalimat+"1 huruf kapital"
        elif angka==0:
            return kalimat+"1 digit angka"
        elif kapital>0 and angka>0:
            return valid+str(angka)+str(kapital)+pw

print(cekPassword("admin"))
print(cekPassword("reload"))
print(cekPassword("powerOff"))
print(cekPassword("cloud24"))
print(cekPassword("Cinema21"))
print(cekPassword("CafeOutDOOR7890"))