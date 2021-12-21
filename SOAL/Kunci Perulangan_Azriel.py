# soal perulangan
pelanggan = []
kendaraan = []
while True:
    print("""\nSilahkan pilih menu dibawah ini:
1. Menambah data
2. Menampilkan data
3. Keluar""")
    inp = int(input("Silahkan masukan pilihan yang Anda inginkan: "))
    if inp == 1:
        nama = input("Masukkan nama pelanggan: ")
        motor = input("Masukkan nama kendaraan: ")
        if nama in pelanggan and motor in kendaraan:
            print("Pelangggan sudah pernah berkunjung.")
        else:
            pelanggan.append(nama)
            kendaraan.append(motor)
            print("Data berhasil ditambahkan")
    elif inp == 2:
        print("----------------------------\nPelanggan      Kendaraan: ")
        nomor = 1
        for i, j in zip(pelanggan, kendaraan):
            print(f"{nomor}.{i}         {j}")
            nomor = nomor + 1
    elif inp == 3:
        print("\nSistem Berhenti...")
        break
    else:
        print("Input tidak valid")
