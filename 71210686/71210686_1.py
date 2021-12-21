a = int(input("Masukkan sisi a : "))
b = int(input("Masukkan sisi b : "))
c = int(input("masukkan sisi c : "))

print()
if a == b == c:
    print("Terdapat 3 sisi yang sama!")
    print("Segitiga tersebut merupakan segitiga sama sisi.")
elif a == b or a == c or b == c:
    if a == b:
        print("Terdapat 2 sisi yang sama, yaitu a dan b!")
    elif a == c:
        print("Terdapat 2 sisi yang sama, yaitu a dan c!")
    elif b == c:
        print("Terdapat 2 sisi yang sama, yaitu b dan c!")
    print("Segitiga tersebut merupakan segitiga sama kaki.")
elif a <= 0 or b <= 0 or c <= 0:
    print("Invalid input!")
elif a != b != c:
    print("Tidak terdapat sisi yang sama!")
    print("Segitiga tersebut merupakan segitiga sembarang.")
