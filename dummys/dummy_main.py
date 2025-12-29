from dummy_battery import dummy_update_soc, calculate_remaining_energy

import time
from dummy_data import (
    dummy_speed,
    dummy_battery_temp,
    dummy_motor_rpm,
    dummy_battery_voltage,
    dummy_fault_flag
)
from hata_kontrol import sistem_kontrol


def main():
    soc = 100.0   

    while True:
        speed = dummy_speed()
        battery_temp = dummy_battery_temp()
        motor_rpm = dummy_motor_rpm()
        battery_voltage = dummy_battery_voltage()
        fault = dummy_fault_flag()

        # SOC GÜNCELLE
        soc = dummy_update_soc(soc)

        # KALAN ENERJİ
        remaining_energy = calculate_remaining_energy(soc)

        print("Speed (km/h):", speed)
        print("Battery Temp (C):", battery_temp)
        print("Motor RPM:", motor_rpm)
        print("Battery Voltage (V):", battery_voltage)
        print(f"Battery SOC (%): {soc:.2f}")
        print(f"Remaining Energy (kWh): {remaining_energy:.2f}")
        print("-" * 30)

        sistem_kontrol(battery_temp, motor_rpm, battery_voltage)

        print("-" * 30)

        # TEK GERÇEK PACKET
        packet = {
            "speed_kmh": speed,
            "battery_temp_c": battery_temp,
            "motor_rpm": motor_rpm,
            "battery_voltage_v": battery_voltage,
            "battery_soc": round(soc, 2),
            "battery_energy_kwh": round(remaining_energy, 2),
            "fault": fault
        }

        print("Telemetry Packet:", packet)
        print("=" * 30)

        time.sleep(1)


if __name__ == "__main__":
    main()
