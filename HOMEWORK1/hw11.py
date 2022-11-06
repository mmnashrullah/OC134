#Definisi fungsi
def faktorial(nilai):
    if nilai <= 1:
        return 1 
    else:
        return nilai * faktorial(nilai - 1) 
    
#Program utama
print("=====Program Rekursi=====")
n = int(input("Masukkan nilai Faktorial yang dicari: "))
for i in range(n - 1):
    print("%d ! = %d" % (i, faktorial(i)))
