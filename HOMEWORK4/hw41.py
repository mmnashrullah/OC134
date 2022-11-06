# -*- coding: utf-8 -*-

# Kalkulator sederhana
# (pertambahan, pengurangan, perkalian, pembagian, pemangkatan, akar) 

Pertambahan = lambda a, b : a + b
Pengurangan = lambda a, b : a - b
Perkalian = lambda a, b : a * b
Pembagian = lambda a, b : a / b
Pemangkatan = lambda a, b : a ** b
Akar = lambda a, b : a ** (1 / b)

def main():
    print("Kalkulator sederhana")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pemangkatan")
    print("6. Akar")
    opt = input("Masukkan mode perhitungan: ")
    
    if (opt) == "1":
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua yang menanbahi: "))
        hasil = Pertambahan(angka1, angka2)
        print("Hasilnya: " + str(hasil))
        
    if (opt) == "2":
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua yang mengurangi: "))
        hasil = Pengurangan(angka1, angka2)
        print("Hasilnya: " + str(hasil))
        
    if (opt) == "3":
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua yang mengali : "))
        hasil = Perkalian(angka1, angka2)
        print("Hasilnya: " + str(hasil))
        
    if (opt) == "4":
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua yang membagi: "))
        hasil = Pembagian(angka1, angka2)
        print("Hasilnya: " + str(hasil))
        
    if (opt) == "5":
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua yang memangkat: "))
        hasil = Pemangkatan(angka1, angka2)
        print("Hasilnya: " + str(hasil))
        
    if (opt) == "6":
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua yang mengakar: "))
        hasil = Akar(angka1, angka2)
        print("Hasilnya: " + str(hasil))

main()    
    
