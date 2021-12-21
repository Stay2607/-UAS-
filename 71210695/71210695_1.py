while True:
    # Program 1
    a = int(input("Masukan sisi a  : "))
    b = int(input("Masukan sisi b  : "))
    c = int(input("Masukan sisi c  : "))

    if a == b == c:
        print("Terdapat 3 sisi yang sama!")
        print("Segitiga tersebut merupakan segitiga sama sisi")
    elif a != b == c:
        print("Terdapat 2 sisi yang sama, yaitu b dan c!")
        print("Segitiga tersebut merupakan segitiga sama kaki")
    else:
        print("Tidak terdapat sisi yang sama!")
        print("Segitiga tersebut merupakan segitiga sembarang")
