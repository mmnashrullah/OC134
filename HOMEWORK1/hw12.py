def ECSAR_Tanah(EC_tanah, SAR_tanah):
    if (EC_tanah < 0):
        if (SAR_tanah <0):
            return('EC dan SAR tidak boleh negatif')
        else:
            return('EC tidak boleh negatif')
    else:
        if (SAR_tanah <0):
            return('SAR tidak boleh negatif')
            
    if (EC_tanah <= 4) :
        if (SAR_tanah <= 13):
            return('Tanah non-salin')
        elif (SAR_tanah > 13):
            return('Tanah sodik')    
    elif (EC_tanah > 4):
        if (SAR_tanah <= 13):
            return('Tanah salin')
        elif (SAR_tanah > 13):
            return('Tanah salin-sodik')
    else:
        pass
    

#Program utama
if __name__ == "__main__":
    a = float(input('Input nilai EC tanah: '))
    b = float(input('Input nilai SAR tanah: '))
    ECSAR_Tanah(a, b)
