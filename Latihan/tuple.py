## Tuple
# Tidak bisa di ubah/ immutable

    # membuat Tuple

print('--- Membuat Tuple ---')
my_tuple = (1, 2, 3, 4)
print(my_tuple)
    # untuk menginisiasi 1 item di dalam Tuple harus menggunakan tanda koma di akhir item tsb.
my_tuple_2 = (1,)
print(type(my_tuple_2))

# Mengakses item Tuple
# seperti pada List dapa mengakses dengan index positif dan negatif, slicing dan indexing
print('\n--- Mengakses anggota Tuple ---')

my_tuple_3 = (1, 'ayub', 2, 'buya', 3, 'cuya')
print('isi item Tuple pertama : ',my_tuple_3[0])
print('isi item Tuple ketiga : ',my_tuple_3[2])
print('isi item Tuple pertama - ke empat : ',my_tuple_3[:5])

# Mengedit Tuple
# Tuple tidak bisa di ubah. Jika di ubah maka akan muncul eror

# my_tuple_3[1] = 9
# print(my_tuple_3)

# menginisiasi multi-variabel dengan Tuple
# Walau tidak bisa melakukan perubahan, tetap bisa menginisiasi anggota Tuple ke dalam variabel-variabel. Hanya saja variabe dan anggota Tuple harus berjumlah sama.

my_tuple_4 = (5, 6, 7) # buat Tuple
a, b, c = my_tuple_4 # inisiasi ke dalam 3 variabel, karena anggota my_tuple_4 ada 3 anggota
print(a)
print(b)
print(c)
print(type(a), type(b), type(c) )