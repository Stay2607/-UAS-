while True:
    # int
    a = int(input("Masukan sisi a :"))
    b = int(input("Masukan sisi b :"))
    c = int(input("Masukan sisi c :"))

    # hitung
    if a == b == c < 0:
        print("INVALID INPUT")
    elif a == b == c:
        print("Terdapat 3 sisi yang sama!")
        print("Segitiga tersebut merupakan segitiga sama sisi.")
    elif a == c < 0:
        print("Terdapat 2 sisi yang sama!", ",yaitu a dan c")
        print("Segitiga tersebut merupakan segitiga sama kaki.")
    elif a == b < 0:
        print("Terdapat 2 sisi yang sama!", ",yaitu a dan b")
        print("Segitiga tersebut merupakan segitiga sama kaki.")
    elif b == c < 0:
        print("Terdapat 2 sisi yang sama!", ",yaitu b dan c")
        print("Segitiga tersebut merupakan segitiga sama kaki.")
    else:
        print("Tidak terdapat sisi yang sama !")
        print("Segitiga tersebut merupakan segitiga sembarang.")
