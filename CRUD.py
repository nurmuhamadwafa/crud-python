#!/usr/bin/python3
# mengubah warna output dengan kode ansi
W = '\033[00m' # warna putih
R = '\033[91m' # warna merah
G = '\033[92m' # warna hijau
# deklarasi variabel dengan tipe data list untuk menyimpan elemen
elemen = []
# fungsi menu untuk menampilkan menu
def menu():
    print('-'*22)
    print('-- List Daftar Menu --')
    print('-'*22)
    print(  '  1. Create\n'\
            '  2. Read\n'\
            '  3. Update\n'\
            '  4. Delete\n'\
            '  0. Keluar'  )
    print('-'*22)
# fungsi create untuk menambahkan elemen baru
def create():
    new_data = input("Masukkan Elemen Baru: ")
    elemen.append(new_data)
    print(f" {G}✔ Elemen Berhasil Ditambahkan.{W}")
# fungsi read untuk menampilkan elemen yang telah ditambahkan
def read():
    # memeriksa apakah ada elemen yang tersimpan
    if len(elemen) == 0:
        print(f' {R}[!] Tidak Ada Elemen Yang Tersimpan!{W}')
    else:
        print('-'*22)
        print("Elemen Yang Tersimpan:")
        for i in range(len(elemen)):
            print(f" {i+1}. {elemen[i]}")
        print('-'*22)
# fungsi update untuk memperbarui elemen
def update():
    # memeriksa apakah ada elemen yang tersimpan
    if len(elemen) == 0:
        print(f' {R}[!] Tidak Ada Elemen Yang Tersimpan!{W}')
    else:
        try:
            index = int(input("Masukkan Nomor Elemen Yang Ingin Diubah: "))
        except ValueError:
            print(f' {R}[!] Input Tidak Valid!{W}')
        # memeriksa kondisi apakah nomor ada dalam elemen
        if 1 <= index <= len(elemen):
            new_data = input("Masukkan Elemen Baru: ")
            elemen[index-1] = new_data
            print(f" {G}✔ Elemen Berhasil Diubah.{W}")
        else:
            print(f' {R}[!] Nomor Tidak Ada Dalam Elemen!{W}')
# fungsi delete untuk menghapus elemen
def delete():
    # memeriksa apakah ada elemen yang tersimpan
    if len(elemen) == 0:
        print(f' {R}[!] Tidak Ada Elemen Yang Tersimpan!{W}')
    else:
        try:
            index = int(input("Masukkan Nomor Elemen Yang Ingin Dihapus: "))
        except ValueError:
            print(f' {R}[!] Input Tidak Valid!{W}')
        # memeriksa kondisi apakah nomor ada dalam elemen
        if 1 <= index <= len(elemen):
            del elemen[index-1]
            print(f' {G}✔ Elemen Berhasil Dihapus.{W}')
        else:
            print(f' {R}[!] Nomor Tidak Ada Dalam Elemen!{W}')
# fungsi main untuk memilih opsi pada menu
def main():
    try:
        menu()
        while True:
            try:
                opsi = int(input('Masukkan Pilihan Menu: '))
            except ValueError:
                print(f' {R}[!] Input Tidak Valid!{W}')
                continue
            if opsi == 1:
                create()
            elif opsi == 2:
                read()
            elif opsi == 3:
                update()
            elif opsi == 4:
                delete()
            elif opsi == 0:
                print(f' {G}✔ Program selesai!{W}')
                break
            else:
                print(f' {R}[!] Pilihan Tidak Tersedia, Pilih Sesuai Menu!{W}')
                return main()
    except KeyboardInterrupt:
        print(f'\n {R}[!] Program Dibatalkan Oleh User!{W}')

if __name__ == '__main__':
    main()