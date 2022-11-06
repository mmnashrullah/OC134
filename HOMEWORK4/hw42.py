# -*- coding: utf-8 -*-

# Menghitung Banyak Faktorial, Permutasi, Kombinasi

def Faktorial(n):
    # n = banyak objek keseluruhan
    if n <= 1:
        return 1 
    else:
        return n * Faktorial(n - 1) 

def Permutasi(n, r):
    # n = banyak objek keseluruhan
    # r = banyak objek yang diberi perlakuan
    return (Faktorial(n) / Faktorial(n - r))
    
def Kombinasi(n, r):
    # n = banyak objek keseluruhan
    # r = banyak objek yang diberi perlakuan
    return (Faktorial(n) / (Faktorial(r) * Faktorial(n - r)))

def main():
    print("Menghitung Banyak Faktorial, Permutasi, Kombinasi")
    print("1. Faktorial")
    print("2. Permutasi")
    print("3. Kombinasi")

    opt = input("Masukkan mode perhitungan: ")
    
    if (opt) == "1":
        angka1 = int(input("Masukkan banyak objek keseluruhan: "))
        hasil = Faktorial(angka1)
        print("Hasilnya: " + str(hasil))
        
    if (opt) == "2":
        angka1 = int(input("Masukkan banyak objek keseluruhan: "))
        angka2 = int(input("Masukkan banyak objek yang diberi perlakuan: "))
        hasil = Permutasi(angka1, angka2)
        print("Hasilnya: " + str(hasil))
        
    if (opt) == "3":
        angka1 = int(input("Masukkan banyak objek keseluruhan: "))
        angka2 = int(input("Masukkan banyak objek yang diberi perlakuan: "))
        hasil = Kombinasi(angka1, angka2)
        print("Hasilnya: " + str(hasil))
        
main()    
    