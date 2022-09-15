## set --> salah satu tipe data yang tidak berurut
# set --> tidak boleh duplikasi, Jika ada maka otomatis akan menghilangkan salah satunya
# set --> tidak  punya index/koordinat

    # membuat set

set_01 = {1, 2, 3}
print('Nilai set_01 : ',set_01)

    # membuat set menggunakan fungsi set()

my_set = set([1,2,3])
print('set menggunakan fungsi set()',my_set)

    # membuat set kosong harus menggunakan fungsi set() tanpa argumen apapun
set_kosong = set()
set_kosong_2 = {} # dianggap dictionary
print(type(set_kosong))
print(type(set_kosong_2))

    # SET tidak mendukung indexing, jadi akan eror jika melakukan indexing maupun slicing

set_ayub = {1, 3, 5, 7,9}
# print(set_ayub[2]) # akan error

    # menambah dan mengubah anggota SET

# update menggunakan fungsi .add()

set_baru = {1, 2, 3, 4, 5}
set_baru.add(0) # nilai baru akan muncul di awal
print('tambah menggunakan method .add()', set_baru)

# update menggunakan fungsi .update()
# update menghilangkan duplikasi
set_baru.update([4, 5, 6, 7, 8])
print('tambah menggunakan method .update()', set_baru)

# Menghapus anggota SET

my_set_2 = {1, 2, 3, 4, 5}

# discard() --> tidak muncul error jika anggota yg ingin di hapus tidak ada
my_set_2.discard(6)
print('Hapus menggunakan discard()', my_set_2)

# remove() --> muncul error jika anggota yang ingin dihapus tidak ada
my_set_2.remove(6)
print('Hapus menggunakan remove()', my_set_2)
