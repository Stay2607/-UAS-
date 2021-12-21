while True:
    a = int(input("\nMasukkan sisi a : "))
    b = int(input("Masukkan sisi b : "))
    c = int(input("Masukkan sisi c : "))
    print()

    if a < 1 or b < 1 or c < 1:
        print("Invalid input!")
    elif a == b and b == c:
        print("Terdapat 3 sisi yang sama!")
        print("Segitiga tersebut merupakan segitiga sama sisi.")
    elif a == b and a != c:
        print("Terdapat 2 sisi yang sama, yaitu a dan b!")
        print("Segitiga tersebut merupakan segitiga sama kaki.")
    elif b == c and a != b:
        print("Terdapat 2 sisi yang sama, yaitu b dan c!")
        print("Segitiga tersebut merupakan segitiga sama kaki.")
    elif a == c and a != b:
        print("Terdapat 2 sisi yang sama, yaitu a dan c!")
        print("Segitiga tersebut merupakan segitiga sama kaki.")
    else:
        print("Tidak terdapat sisi yang sama!")
        print("Segitiga tersebut merupakan segitiga sembarang.")
