# -*- coding: utf-8 -*-

ulangProgram = ""
  
def main():  
    init_sel = int(input("Jumlah sel mula - mula: "))
    wkt_inkubasi = int(input("Lama waktu inkubasi (dalam jam): "))
    
    try:
        for i in range(wkt_inkubasi + 1):
            if i <= 0:
                print("Jumlah sel pada jam ke-%d adalah %d sel." % 
                      ((i), (init_sel)))
            elif i == 1:
                print("Jumlah sel pada jam ke-%d adalah %d sel" % 
                      ((i), (init_sel * ((2 ** ((60 / 15)))))))
            elif i > 1:
                print("Jumlah sel pada jam ke-%d adalah %d sel" % 
                      ((i), (init_sel * (((2 ** ((60 / 15)))) ** (i)))))
            else:
                print("Waktu inkubasi tidak boleh kurang dari nol.")
    except(ValueError, ZeroDivisionError):
        print("Ada kesalahan")
    finally:    
        ulangProgram = input("Ingin mengulang program (y/t)?: ")
        while (ulangProgram) == "y":
            ulangProgram = ""
            main()
        else:
            pass
    
main()
