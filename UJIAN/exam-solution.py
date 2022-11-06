# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 12:04:56 2022

@author: MALIK
"""

def HitungTm(Seq):
    G = (Seq.count("G") + Seq.count("g"))
    C = (Seq.count("C") + Seq.count("c"))
    A = (Seq.count("A") + Seq.count("a"))
    T = (Seq.count("T") + Seq.count("t"))
    Tm = (4 * (G + C)) + (2 * (A + T))
    return Tm

def HitungTa(Tm_primer, Tm_product):
    Tm_primer = HitungTm(Tm_primer)
    Tm_product = HitungTm(Tm_product)
    Ta = (0.3 * Tm_primer) + (0.7 * Tm_product) - 14.9
    return Ta

def DNAtoMRNA(DNASeq):
    liDNASeq = list(DNASeq)
    
    for i in range(len(liDNASeq)):
        if ((liDNASeq[i]) == "T"):
            liDNASeq[i] = "U"
    
    BlankString = ""
    GetSeq = BlankString.join(liDNASeq)
    return GetSeq
    
def GCContent(Seq):
    G = (Seq.count("G") + Seq.count("g"))
    C = (Seq.count("C") + Seq.count("c"))
    A = (Seq.count("A") + Seq.count("a"))
    T = (Seq.count("T") + Seq.count("t"))
    GC = round((((G + C) / (A + T + G + C)) * 100), 1)
    return GC

def ATContent(Seq):
    G = (Seq.count("G") + Seq.count("g"))
    C = (Seq.count("C") + Seq.count("c"))
    A = (Seq.count("A") + Seq.count("a"))
    T = (Seq.count("T") + Seq.count("t"))
    AT = round((((A + T) / (A + T + G + C)) * 100), 1)
    return AT

def CekKualitasPrimer(Seq):
    if ((len(Seq) >= 18) and (len(Seq) <= 22)):
        if ((GCContent(Seq) >= 40) and (GCContent(Seq) <= 60)):
            if ((HitungTm(Seq) >= 52) and (HitungTm(Seq) <= 58)):
                return "Baik"
            else:
                return "Buruk"
        else:
            return "Buruk"
    else:
        return "Buruk"

def main():
    print("===Selamat Datang Di Program Kalkulator Primer===")
    print("=================================================")
    a = input("Masukkan judul sampel: ")
    b = input("Masukkan sekuen DNA sampel: ")
    c = input("Masukkan sekuen primer forward: ")
    d = input("Masukkan sekuen primer reverse: ")
    print("=================================================")
    print("")
    try:
        print("===============   [Sekuen DNA]   ================")
        print("Nama Sampel: " + a)
        print("Sekuen DNA: " + b)
        print("Sekuen mRNA: " + DNAtoMRNA(b))
        print("")
        print("=============== [Primer Forward] ================")
        print("Panjang primer = " + str(len(c)) + " bp")
        print("Konten AT = " + str(ATContent(c)) + " AT %")
        print("Konten GC = " + str(GCContent(c)) + " GC %")
        print("Tm primer = " + str(HitungTm(c)) + "°C")
        print("Kualitas primer = " + CekKualitasPrimer(c))
        print("")
        print("=============== [Primer Reverse] ================")
        print("Panjang primer = " + str(len(d)) + " bp")
        print("Konten AT = " + str(ATContent(d)) + " AT %")
        print("Konten GC = " + str(GCContent(d)) + " GC %")
        print("Tm primer = " + str(HitungTm(d)) + "°C")
        print("Kualitas primer = " + CekKualitasPrimer(d))
    except:
        print("Ada Error. Cek Kembali data inputan")

    ulangProgram = input("Ingin mengulang program (y/t)?: ")
    while (ulangProgram) == "y":
        main()
    else:
        pass
    
main()


    
