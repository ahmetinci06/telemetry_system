# 🚗 AVT VCU Firmware

<div align="center">

**Vehicle Control Unit for TÜBİTAK Efficiency Challenge**

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()
[![Platform](https://img.shields.io/badge/platform-STM32G491RE-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

</div>

---

## 🎯 Overview

High-efficiency Vehicle Control Unit firmware for the **Elektromobil** category of the TÜBİTAK Efficiency Challenge. Designed for energy consumption under **130 Wh/km**.

```
┌─────────────────────────────────────────────────────────────┐
│                       VCU (STM32G491RE)                     │
│                                                             │
│   INPUTS              LOGIC               OUTPUTS           │
│   ───────            ─────               ────────           │
│   • Pedal (ADC)  ──► State Machine ──►  • Torque (CAN/UART) │
│   • Brake (GPIO) ──► Safety Checks ──►  • LED Status        │
│   • BMS (CAN)    ──► Energy Mgmt   ──►  • Telemetry         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚡ Features

| Module                | Description                                         | Status     |
| --------------------- | --------------------------------------------------- | ---------- |
| **Pedal Input**       | ADC with 16x oversampling, wire-break detection     | ✅ Done    |
| **State Machine**     | OFF → READY → DRIVE → FAULT                         | ✅ Done    |
| **FDCAN**             | 500 kbit/s, BMS/VESC communication                  | ✅ Done    |
| **Safety**            | Brake interlock, fault handling, timeout monitoring | ✅ Done    |
| **Energy Monitoring** | Wh tracking, efficiency calculation                 | 📋 Planned |

---

## 🛠️ Hardware

| Component | Specification                   |
| --------- | ------------------------------- |
| **MCU**   | STM32G491RE (Nucleo-64)         |
| **Pedal** | 0-5V potentiometer → PA0        |
| **Brake** | Digital input → PA1             |
| **CAN**   | FDCAN1 @ 500 kbit/s (PA11/PA12) |
| **LED**   | Green LED → PA5                 |

---

## 📂 Project Structure

```
AVT-VCU-DEV/
├── 📁 Core/
│   ├── Inc/           # Headers
│   │   ├── vcu_pedal.h
│   │   ├── vcu_state.h
│   │   └── vcu_can.h
│   └── Src/           # Source files
│       ├── main.c
│       ├── vcu_pedal.c
│       ├── vcu_state.c
│       └── vcu_can.c
├── 📁 docs/           # Documentation
├── 📁 Drivers/        # STM32 HAL
└── 📄 AVT-VCU-DEV.ioc # CubeMX project
```

---

## 📚 Documentation

| Document                                | Description                             |
| --------------------------------------- | --------------------------------------- |
| [👥 Team](docs/TEAM.md)                 | **Team assignments & responsibilities** |
| [📋 Task Tracker](docs/TASK-TRACKER.md) | Development progress                    |
| [🚀 Next Steps](docs/NEXT-STEPS.md)     | Hardware testing & future dev           |
| [🎛️ Pedal Module](docs/vcu_pedal.md)    | ADC, filtering, fault detection         |
| [🔄 State Machine](docs/vcu_state.md)   | OFF/READY/DRIVE/FAULT states            |
| [📡 CAN Module](docs/vcu_can.md)        | BMS/VESC communication                  |
| [🔌 Arduino ESC](docs/arduino-esc.md)   | Arduino Nano ESC integration            |
| [🏗️ Architecture](docs/architecture.md) | System design & data flow               |

---

## 🚀 Quick Start

### 1. Clone & Open

```bash
git clone https://github.com/your-org/AVT-VCU-DEV.git
# Open in STM32CubeIDE
```

### 2. Build

```
Project → Build All (Ctrl+B)
```

### 3. Flash

```
Run → Debug As → STM32 Application
```

---

## 📊 State Machine

```
          ┌─────────┐
          │   OFF   │◄─────────────────────┐
          └────┬────┘                      │
               │ Power On                  │ Clear Fault
               ▼                           │
          ┌─────────┐                 ┌────┴────┐
          │  READY  │────────────────►│  FAULT  │
          └────┬────┘  Any Fault      └─────────┘
               │                           ▲
               │ Start + No Brake          │
               ▼                           │
          ┌─────────┐                      │
          │  DRIVE  │──────────────────────┘
          └─────────┘  Any Fault
```

---

## 🔧 Configuration

Key constants in header files:

```c
// vcu_pedal.h
#define PEDAL_ADC_MIN_VALID   200   // Wire-break threshold
#define PEDAL_ADC_MAX_VALID   3800  // Short-circuit threshold

// vcu_state.h
#define TIMEOUT_BMS_MS        500   // BMS heartbeat timeout
#define TIMEOUT_VESC_MS       200   // VESC response timeout

// main.c
#define MAX_MOTOR_CURRENT_A   50.0f // Maximum torque
```

---

## 🏁 Competition Targets

| Metric   | Target      | Methods                    |
| -------- | ----------- | -------------------------- |
| Energy   | < 130 Wh/km | Efficient mapping, regen   |
| Safety   | Zero faults | Redundant checks, watchdog |
| Response | < 10ms      | 100Hz main loop            |

---

## 📜 License

MIT License - See [LICENSE](LICENSE) for details.

---

<div align="center">

**AVT Racing Team** | TÜBİTAK Efficiency Challenge 2025

</div>
