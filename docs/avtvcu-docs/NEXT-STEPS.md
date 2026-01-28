# VCU Development: Next Steps

> Guide for continuing VCU firmware development after Sprint 1-2 completion

---

## 🎯 Current Status

| Module            | Status      | Files           |
| ----------------- | ----------- | --------------- |
| Pedal Input       | ✅ Complete | `vcu_pedal.h/c` |
| State Machine     | ✅ Complete | `vcu_state.h/c` |
| FDCAN (BMS/VESC)  | ✅ Complete | `vcu_can.h/c`   |
| Energy Monitoring | 📋 Next     | -               |
| Regen Braking     | 📋 Planned  | -               |
| Telemetry         | 📋 Planned  | -               |

---

## Step 1: Hardware Testing

### 1.1 Flash the Firmware

```bash
# In STM32CubeIDE:
# 1. Connect ST-Link to Nucleo-G491RE
# 2. Run > Debug As > STM32 Application
# Or: Run > Run As > STM32 Application (no debugging)
```

### 1.2 Test Checklist

| Test              | Expected Result                 | Pass? |
| ----------------- | ------------------------------- | ----- |
| **Power On**      | LED on, state = READY           |       |
| **Pedal 0%**      | No torque command sent          |       |
| **Pedal 50%**     | 25A current command             |       |
| **Pedal 100%**    | 50A current command             |       |
| **Wire Break**    | LED on, state = FAULT, 0 torque |       |
| **Short Circuit** | LED on, state = FAULT, 0 torque |       |
| **Brake Press**   | 0 torque even if pedal pressed  |       |
| **BMS Timeout**   | FAULT after 500ms no CAN        |       |

### 1.3 Debug with UART

Add printf output for debugging (already configured on PA2/PA3):

```c
// In main.c USER CODE section:
printf("State: %s, Pedal: %.1f%%, Fault: 0x%08lX\r\n",
       VCU_State_GetName(VCU_State_GetCurrent(&state_machine)),
       VCU_Pedal_GetPercent(&pedal),
       state_machine.fault_code);
```

### 1.4 CAN Bus Testing

**Using USB-CAN adapter or second MCU:**

1. Send BMS messages (0x100-0x104) every 100ms
2. Verify VCU receives and parses correctly
3. Monitor 0x300 (VCU Status) messages
4. Test timeout by stopping BMS messages

---

## Step 2: Energy Monitoring Module

### 2.1 Create Files

| File                    | Purpose        |
| ----------------------- | -------------- |
| `Core/Inc/vcu_energy.h` | Header         |
| `Core/Src/vcu_energy.c` | Implementation |
| `docs/vcu_energy.md`    | Documentation  |

### 2.2 Features to Implement

```c
typedef struct {
    float wh_consumed;       // Total Wh consumed
    float wh_regen;          // Total Wh regenerated
    float distance_m;        // Distance traveled (from VESC RPM)
    float wh_per_km;         // Current efficiency
    float avg_power_w;       // Average power consumption
} EnergyData_t;
```

**Functions:**

- `VCU_Energy_Init()` - Reset counters
- `VCU_Energy_Update(voltage, current, dt)` - Integrate power
- `VCU_Energy_GetEfficiency()` - Return Wh/km
- `VCU_Energy_GetSOC()` - Estimate remaining range

### 2.3 Integration Points

```c
// In main loop:
float voltage = VCU_CAN_GetBMSData()->pack_voltage;
float current = VCU_CAN_GetBMSData()->pack_current;
VCU_Energy_Update(&energy, voltage, current, 0.01f); // 10ms loop

// For telemetry:
VCU_CAN_SendEnergyData(&energy);
```

---

## Step 3: Push to Main Branch

### 3.1 Pre-Push Checklist

- [ ] All modules compile without warnings
- [ ] Hardware tested and verified
- [ ] Documentation updated
- [ ] TASK-TRACKER.md reflects current status
- [ ] No debug code left in production

### 3.2 Git Workflow

```bash
# Check status
git status

# Stage all changes
git add -A

# Commit with descriptive message
git commit -m "feat: Complete Phase 1 - Pedal, State Machine, FDCAN

- Added vcu_pedal module with fault detection
- Added vcu_state module (OFF/READY/DRIVE/FAULT)
- Added vcu_can module for BMS/VESC communication
- Configured FDCAN1 at 500 kbit/s (PA11/PA12)
- Integrated all modules in main.c
- Added comprehensive documentation"

# Push to main
git push origin main
```

### 3.3 Branch Strategy for Future

```
main (stable, tested)
├── develop (integration branch)
│   ├── feature/energy-monitoring
│   ├── feature/regen-braking
│   └── feature/telemetry
```

---

## 📂 File Structure After Completion

```
AVT-VCU-DEV/
├── Core/
│   ├── Inc/
│   │   ├── main.h
│   │   ├── vcu_pedal.h      ✅
│   │   ├── vcu_state.h      ✅
│   │   ├── vcu_can.h        ✅
│   │   └── vcu_energy.h     📋 Next
│   └── Src/
│       ├── main.c           ✅ (integrated)
│       ├── vcu_pedal.c      ✅
│       ├── vcu_state.c      ✅
│       ├── vcu_can.c        ✅
│       └── vcu_energy.c     📋 Next
├── docs/
│   ├── README.md            ✅
│   ├── TASK-TRACKER.md      ✅
│   ├── architecture.md      ✅
│   ├── vcu_pedal.md         ✅
│   ├── vcu_state.md         ✅
│   ├── vcu_can.md           ✅
│   ├── vcu_energy.md        📋 Next
│   └── NEXT-STEPS.md        ✅ This file
└── Debug/
    └── AVT-VCU-DEV.elf      ✅ (buildable)
```

---

## 🔧 Quick Reference

### Key Constants (in headers)

| Constant              | Value | Location    |
| --------------------- | ----- | ----------- |
| `MAX_MOTOR_CURRENT_A` | 50.0f | main.c      |
| `PEDAL_ADC_MIN_VALID` | 200   | vcu_pedal.h |
| `PEDAL_ADC_MAX_VALID` | 3800  | vcu_pedal.h |
| `TIMEOUT_BMS_MS`      | 500   | vcu_state.h |
| `TIMEOUT_VESC_MS`     | 200   | vcu_state.h |
| `VESC_CAN_ID`         | 0x00  | vcu_can.h   |

### Pin Configuration

| Pin  | Function           |
| ---- | ------------------ |
| PA0  | ADC1_IN1 (Pedal)   |
| PA1  | Brake Input (GPIO) |
| PA5  | LED Green          |
| PA11 | FDCAN1_RX          |
| PA12 | FDCAN1_TX          |

### CAN Message IDs

| ID          | Direction | Content       |
| ----------- | --------- | ------------- |
| 0x100-0x104 | RX        | BMS Status    |
| 0x9XX       | RX        | VESC Status   |
| 0x1XX       | TX        | VESC Commands |
| 0x300       | TX        | VCU Status    |
