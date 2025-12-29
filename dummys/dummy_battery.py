

BATTERY_CAPACITY_KWH = 50.0  #sabit kapasite

def dummy_update_soc(soc):
    """
    Dummy SOC düşüşü
    """
    soc -= 0.05  # her döngü %0.05 düşsün
    if soc < 0:
        soc = 0.0
    return soc


def calculate_remaining_energy(soc):
    """
    SOC'den kalan enerjiyi hesapla
    """
    return BATTERY_CAPACITY_KWH * (soc / 100.0)
