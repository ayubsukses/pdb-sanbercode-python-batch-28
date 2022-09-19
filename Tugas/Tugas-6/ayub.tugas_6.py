'''Soal 1: While Loop dan For Loop

- Apa perbedaan while loop dan for loop?
    jawab :
        - for loop --> 1. mengulangi kode yang sudah diketahui banyak perulangannya
        - while loop --> perulangan yang memiliki syarat dan tidak tentu berapa banyak perulangannya
- Berikan contoh sederhana cara menggunakan while loop dan for loop
    - for loop --> 
        for angka in deret_angka :
            print('isi', angka)
    - while loop -->
        while nama == 'ayub' :
            print('nama sesuai')
        
'''




# soal 4

obj_list= [1, 16, 11, 10, 5]
for index, angka in enumerate(obj_list):
    print(angka * index)
