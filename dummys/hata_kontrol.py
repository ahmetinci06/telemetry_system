

def sistem_kontrol(temp, rpm, voltage):
    """
    Bu fonksiyon sensör verilerini alır ve limit dışına çıkarsa
    ekrana uyarı basar.
    """
    
    hata_var_mi = False

    
    if temp > 53.0:
        print(f"!!! ALARM: Batarya Isısı Çok Yüksek ({temp:.1f}°C)")
        hata_var_mi = True


    if rpm > 10000:
        print(f"!!! ALARM: Motor RPM Sınırı Aşıldı ({rpm})")
        hata_var_mi = True
    

    if voltage < 310.0:
        print(f"!!! ALARM: Voltaj Kritik Düşük ({voltage:.1f} V)")
        hata_var_mi = True
    elif voltage > 410.0:
        print(f"!!! ALARM: Voltaj Çok Yüksek ({voltage:.1f} V)")
        hata_var_mi = True
    
    return hata_var_mi