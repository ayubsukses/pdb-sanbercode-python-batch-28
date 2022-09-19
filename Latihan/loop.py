# for loop

nama_buah = ['apel', 'jeruk', 'mangga', 'alpukat', 'nanas']
for buah in nama_buah :
    print('buah yang tersedia :', buah)
print('stok buah', len(nama_buah))

for index, angka in enumerate(range(0, 11, 2)) :
    print(f"angka {angka} ada di index ke-{index}")

# while loop

jawab = 'ya'
hitung = 0

while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")

print(f"Total perulagan: {hitung}") 