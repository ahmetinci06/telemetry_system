import random

CAN_IDS = {
    "speed_kmh": 0x101,
    "battery_temp_c": 0x201,
    "motor_rpm": 0x301,
    "battery_voltage_v": 0x401,
}

def dummy_speed():
    return round(random.uniform(0, 120), 1)

def dummy_battery_temp():
    return round(random.uniform(20, 60), 1)

def dummy_motor_rpm():
    return random.randint(0, 12000)

def dummy_battery_voltage():
    return round(random.uniform(300, 420), 1)

def dummy_fault_flag():
    return random.choice(["OK", "OVERTEMP", "OVERVOLTAGE", "UNDERVOLTAGE"])


def dummy_telemetry_packet():
    """
    Logger için tek paket (dict) üretir
    """
    return {
        "speed_kmh": dummy_speed(),
        "battery_temp_c": dummy_battery_temp(),
        "motor_rpm": dummy_motor_rpm(),
        "battery_voltage_v": dummy_battery_voltage(),
        "fault": dummy_fault_flag()
    }