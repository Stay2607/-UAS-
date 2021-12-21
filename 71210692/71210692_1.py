while True:
    a = input("Masukkan sisi a : ")
    b = input("Masukkan sisi b : ")
    c = input("Masukkan sisi c : ")
    print("\n")
    if a or b or c < 0:
        print("Invalid input!")
    else:
        if a == b == c:
            print("Terdapat 3 sisi yang sama!")
            print("Segitiga tersebut merupakan segitiga sama sisi.")
        elif a == b != c:
            print("terdapat 2 sisi yang sama, yaitu a dan b!")
            print("Segitiga tersebut merupakan segitiga sama kaki.")
        elif b == c != a:
            print("terdapat 2 sisi yang sama, yaitu b dan c!")
            print("Segitiga tersebut merupakan segitiga sama kaki.")
        elif a == c != b:
            print("terdapat 2 sisi yang sama, yaitu a dan c!")
            print("Segitiga tersebut merupakan segitiga sama kaki.")
        else:
            print("Tidak terdapat sisi yang sama!")
            print("Segitiga tersebut merupakan segitiga sembarang.")
