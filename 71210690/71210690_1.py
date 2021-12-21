while True:
    a = int(input("Masukkan sisi a : "))
    b = int(input("Masukkan sisi b : "))
    c = int(input("Masukkan sisi c : "))
    if (a == b) and (b == c):
        print("")
        print("Terdapat 3 sisi yang sama!")
        print("Segitiga tersebut merupakan segitiga sama sisi.")
    elif (a < 1) and (b < 1) and (c < 1):
        print("Invalid input!")
    elif (a != b) and (a != c) and (b != a) and (b != c) and (c != a) and (c != b):
        print("")
        print("Tidak terdapat sisi yang sama!")
        print("Segitiga tersebut merupakan segitiga sembarang.")
    elif (a != b) and (b == c):
        print("")
        print("Terdapat 2 sisi yang sama, yaitu b dan c!")
        print("Segitiga tersebut merupakan segitiga sama kaki.")
    elif (a == b) and (a != c):
        print("")
        print("Terdapat 2 sisi yang sama, yaitu a dan b!")
        print("Segitiga tersebut merupakan segitiga sama kaki.")
    else:
        print("")
        print("Terdapat 2 sisi yang sama, yaitu a dan c!")
        print("Segitiga tersebut merupakan segitiga sama kaki.")
