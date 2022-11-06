# -*- coding: utf-8 -*-

air = float(input("Masukkan nilai salinitas air uji (dalam %): "))

if (air < 0.05):
    print("Air Tawar")
if (air >= 0.05) and (air <= 3):
    print("Air Payau")
if (air >= 3) and (air <= 5):
    print("Saline")
if (air > 5):
    print("Brine")
