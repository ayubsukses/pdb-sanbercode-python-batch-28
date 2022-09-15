## Dictionary --> Terdiri dari pasangan key : value
# tidak memiliki index

    # membuat Dictionary
print('--- Latihan Dictionary ---')
my_dict = {'nama' : 'Ayub', 'umur' : 21}

    # membuat dictionary integer
dict_integer = {1 : 'satu', 2 : 'dua'}
print('dictionary key integer 1 : ', dict_integer[1])

    # membuat dictionary campuran
dict_campuran = {'nama':'ayub', 1 : 'satu', 'list_dicti': [1, 2, 3]}
print('dictionary campuran  : ', dict_campuran)

    # Akses dictionary
print('value dari nama : ', my_dict['nama'])
print('value dari umur : ', my_dict['umur'])

   # Akses dictionary dengan fungsi get()

print('Akses dictionary dengan get() : ', my_dict.get('nama'))


print('\n --- Menambah/update dictionary ---')
my_dict_2 = {'nama' : 'ayub', 'umur' : 40}
print('dictionary awal - awal : ' ,my_dict_2)

# update usia
print('\n -- update usia --')
my_dict_2['umur'] = 21
print('Mengubah umur menjadi 21 : ', my_dict_2['umur'])

# tambah alamat baru
print('\n -- tambah alamat --')
my_dict_2['alamat'] = 'banbet'
print('Tambah alamat : ', my_dict_2)


print('\n --- Menghapus anggota dictionary ---')

my_dict_3 = {'nama' : 'ayub', 'kelas ' : 'CE-3C', 'umur' : 21}

print('awal- awal dictionary: ', my_dict_3)

    # hapus dengan pop() --> menghapus berdasarkan key
# my_dict_3.pop('umur')
# print('setelah di hapus dengan pop() : ', my_dict_3)

    # hapus dengan clear() --> menghapus seluruh item
# my_dict_3.clear()
# print('hapus dengan clear() : ', my_dict_3)

    #  hapus dengan del() --> hapus berdasarkan key, jika tidak memasukkan key, maka seluruh dictionary akan di hapus
# del my_dict_3['nama'] 
# print('hapus dengan del : ', my_dict_3)

    # hapus dengan del tanpa nama key
# del my_dict_3
# print('hapus dengan del tanpa masukkan key : ', my_dict_3)