# list ---> tipe data yang dapat menampung/menyimpan beberapa nilai di dalamnya
# list ---> bisa menampung/menyimpan 1 tipe data atau lebih dari 1 tipe data (campuran)
# list --> setiap item di pisah oleh koma (,)
# list --> bisa di ubah
# list --> bisa ada list di dalam list

# membuat list kosong

contoh_list_kosong =[]
print('--contoh list kosong--')
print('contoh list kosong :', contoh_list_kosong)

#  list berisi string

contoh_list_string = ['Ayub', 'Sukses', '2025']
print('\n--contoh list berisi string--')
print('contoh list berisi string:', contoh_list_string)

#  list berisi integer

contoh_list_integer = [1, 2, 3]
print('\n--contoh list berisi integer--')
print('contoh list berisi integer :', contoh_list_integer)

# list campuran (list di dalam list)

contoh_list_campuran = ['Ayub', [contoh_list_integer]]
print('\n--contoh list campuran--')
print('contoh list campuran :', contoh_list_campuran)


 ## Mengakses nilai list
   # subsetting list
nama_kawan = ['Ronaldo', 'Suarez', 'Navas', 'Salah', 'Mane']
print('\n--Mengakses item list--')
print('Index ke - 1 : ', nama_kawan[1])
print('Index ke - 3 : ', nama_kawan[3])


    # index negatif
print('\n--Mengakses item list dari belakang (index negatif)--')
print('Index terakhir : ', nama_kawan[-1])

    # memotong (slicing)
print('\n--Mengakses item list sampe index ke - 3 --')
print('Index 0 - 3 : ', nama_kawan[:3])

print('\n--Mengakses item list sampe index ke 1 - 3 --')
print('Index 1 - 3 : ', nama_kawan[1:3])

print('\n--Mengakses item list terakhir -1 : -3 --')
print('Index -1 : -3 : ', nama_kawan[-1:-3])


## Mengganti  nilai list
print('\n--Mengganti nilai list--\n')
nama_barang = ['Kursi', 'Meja', 'Gelas', 'Piring']
print('List sebelum di ganti : ', nama_barang)
    
        # ganti item ke 2
nama_barang[1] = 'Dispenser'
print('list setelah di ganti : ', nama_barang)

        # ganti item sekali banyak
nama_barang[1:2] = ['Aqua', 'Sendal']
print('list setelah di ganti banyak : ', nama_barang)

## Menambah anggota List
    # .append() --> menambahkan item dari belakang
    # .prepend() --> menambah item dari depan
    # .insert() --> menambah item berdasarkan index tertentu

print('\n--Menambah nilai list--\n')
nama_buah = ['Apel', 'Jeruk', 'Mangga']

 # tambah 'kelapa' dengan .append()
print('list awal-awal : ', nama_buah)
nama_buah.append('kelapa')
print('tambah item list .append() : ', nama_buah)

 # tambah 'Nanas' dengan .insert()
print('list awal-awal : ', nama_buah)
nama_buah.insert(0, 'nanas')
print('tambah item list dengan method .insert() : ', nama_buah)

 # tambah 'Nanas' dengan .extend()
print('list awal-awal : ', nama_buah)
nama_buah.extend(['Manggis', 'Semangka', 'Sawit'])
print('tambah item list dengan method .extend() : ', nama_buah)

## Menghapus anggota List
    # del() --> menghapus berdasarkan index yang telah di tentukan. Juga bisa menghapus seluruh item
    # remove() --> menghapus item yang telah ditentukan.
    # pop() --> menghapus item berdasarkan index yang ditentukan. Jika index tidak di tentukan maka item yang paling akhir akan di hapus.
    # clear() --> menghapus/mengosongkan item list. tapi list itu masih ada dalam bentuk list kosong 



print('\n--Menghapus nilai list--\n')

my_list = ['Ayub', 'Ronald', 'Cuya', 'Dodi']

print('List awal-awal : ', my_list)
del (my_list[0])
print('hapus item list dengan method del(): ', my_list)

# print('List awal-awal : ', my_list)
# my_list.remove('Ayub')
# print('hapus item list dengan method remove(): ', my_list)


# print('List awal-awal : ', my_list)
# my_list.pop()
# print("hapus item list dengan method .pop('cuya') : ",my_list)

# print('List awal-awal : ', my_list)
# my_list.clear()
# print("hapus item list dengan method .clear() : ", my_list)

## Some function di dalam list
print('\n--Some Function di dalam list--\n')

    # len() --> menghitung panjang list

list_baru = ['a', 'b','c', 'd']
print('panjang dari list_baru : ', len(list_baru))

    # sorted() --> mengurutkan item list
list_new = [1, 2, 3, 4, 6, 8, 7]
print('list_new sebelum diurutkan : ', list_new)
print('list_new setelah diurutkan : ', sorted(list_new))

    # copy() --> mengcopy suatu nilai list ke dalam list baru

a = [10, 11, 12]
b = a.copy()
print(a)
print(b)

# melakukan manipulasi nilai list b

b.append(13)
print(b)
