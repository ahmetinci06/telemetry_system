# AVT VCU Software Documentation

> **Vehicle Control Unit firmware for TÜBİTAK Efficiency Challenge (Elektromobil)**

---

## 📁 Project Structure

```
AVT-VCU-DEV/
├── Core/
│   ├── Inc/                    # Header files
│   │   ├── main.h              # CubeMX generated
│   │   ├── vcu_pedal.h         # Pedal module ✅
│   │   └── vcu_state.h         # State machine ✅
│   └── Src/                    # Source files
│       ├── main.c              # Main application
│       ├── vcu_pedal.c         # Pedal module ✅
│       └── vcu_state.c         # State machine ✅
├── Drivers/                    # STM32 HAL drivers
├── docs/                       # Documentation
│   ├── README.md               # This file
│   ├── TASK-TRACKER.md         # Development progress
│   ├── vcu_pedal.md            # Pedal module docs
│   └── architecture.md         # System architecture
└── AVT-VCU-DEV.ioc             # CubeMX project
```

---

## 📖 Documentation Index

| Document                             | Description                                    |
| ------------------------------------ | ---------------------------------------------- |
| [TASK-TRACKER.md](./TASK-TRACKER.md) | Development progress & sprint tracking         |
| [NEXT-STEPS.md](./NEXT-STEPS.md)     | **Hardware testing, future development guide** |
| [vcu_pedal.md](./vcu_pedal.md)       | Pedal input module API & usage                 |
| [vcu_state.md](./vcu_state.md)       | State machine module (OFF/READY/DRIVE/FAULT)   |
| [vcu_can.md](./vcu_can.md)           | FDCAN communication (BMS/VESC)                 |
| [architecture.md](./architecture.md) | System architecture & data flow                |

---

## 🎯 Competition Target

| Metric            | Target      |
| ----------------- | ----------- |
| **Distance**      | 22.5 km     |
| **Time**          | 29 minutes  |
| **Energy Budget** | 3 kWh max   |
| **Efficiency**    | < 130 Wh/km |

---

## 🛠 Development Status

### Completed ✅

- [x] ADC1 with 16x hardware oversampling
- [x] Pedal input module with safety interlocks
- [x] Wire-break / short-circuit detection
- [x] Low-pass filtering
- [x] Brake input (PA1)
- [x] 100Hz main loop
- [x] State machine (OFF/READY/DRIVE/FAULT)
- [x] Fault handling with pedal fault linkage

### In Progress 🔄

- [ ] FDCAN communication (BMS/VESC)
- [ ] Energy monitoring

### Planned 📋

- [ ] Regenerative braking optimization
- [ ] Telemetry (UART → ESP32/LoRa)
- [ ] Driver coaching system
- [ ] Data logging to SD card

---

## 🔧 Build Instructions

1. Open `AVT-VCU-DEV.ioc` in **STM32CubeMX**
2. Generate code (if peripheral changes needed)
3. Open project in **STM32CubeIDE**
4. Build: `Project → Build Project` (Ctrl+B)
5. Flash to target NUCLEO-G491RE

---

## 📐 Hardware Configuration

| Peripheral | Pin | Function                   |
| ---------- | --- | -------------------------- |
| ADC1_IN1   | PA0 | Pedal sensor input         |
| GPIO_Input | PA1 | Brake switch (active high) |
| LED        | PA5 | Status indicator           |
| LPUART1_TX | PA2 | Debug/Telemetry            |
| LPUART1_RX | PA3 | Debug/Telemetry            |
| FDCAN1_TX  | PB9 | CAN bus (planned)          |
| FDCAN1_RX  | PB8 | CAN bus (planned)          |

---

## 📚 Related Documents

- [AGENTS.md](../AGENTS.md) - Coding standards & rules
- [README.md](../README.md) - Project overview
- [DEV-PLAN.md](../DEV-PLAN.md) - Full development roadmap
