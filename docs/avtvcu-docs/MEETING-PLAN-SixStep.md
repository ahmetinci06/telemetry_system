# AVT VCU - Six-Step Motor Control Discussion

**Date:** December 2025  
**Topic:** FOC to Six-Step Conversion Planning

---

## 📋 Agenda

### 1. Current State Review (5 min)
- VCU firmware status: Pedal, State Machine, FDCAN ✅
- Current motor control: External VESC via CAN torque commands
- Available hardware: STM32G491RE Nucleo + [TBD driver board]

### 2. Proposed Change Overview (10 min)
- Replace VESC → Direct six-step commutation from STM32
- Reference: Arduino ESC example (`B-IR2110-DRV-01MBR-V1.0.ino`)
- Benefits: Lower cost, full control, single MCU

### 3. Hardware Discussion (15 min)

| Topic | Question | Options |
|-------|----------|---------|
| **Driver IC** | What driver board? | NCP5106B / IR2110 / DRV8301 |
| **Motor** | Specs? | Voltage, poles, Hall wiring |
| **Power Stage** | MOSFETs selected? | [TBD] |
| **PCB** | Custom or off-shelf? | [TBD] |

### 4. Integration Architecture (10 min)

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A** | VCU does motor control | Single MCU, low latency | Complex, safety-critical |
| **B** | Arduino ESC slave | Simple, separate concerns | 2 MCUs, comm latency |
| **C** | Hybrid | Fallback to VESC | Most complex |

**Decision needed:** Which option?

### 5. STM32 Pin Mapping (5 min)

From handwritten notes:
- PWM: D8-D13 range (6 outputs)
- Hall: 3 inputs
- CAN: D0-D1

**Confirm:** Are these fixed by hardware or flexible?

### 6. Expected Questions / Action Items

| # | Question | Answer | Owner |
|---|----------|--------|-------|
| 1 | Integration option (A/B/C)? | | |
| 2 | Driver IC model? | | |
| 3 | Motor voltage/poles? | | |
| 4 | PWM frequency (15-20kHz)? | | |
| 5 | Keep VESC CAN as fallback? | | |
| 6 | Pin mapping confirmed? | | |
| 7 | Dead time requirement? | 1.5µs default | |
| 8 | Current sensing needed? | | |

---

## 🔜 Next Steps (After Meeting)

1. [ ] Finalize hardware selection
2. [ ] Confirm STM32 pin mapping
3. [ ] Update CubeMX with TIM1 PWM + Hall GPIO
4. [ ] Create `vcu_motor.c`, `vcu_hall.c`, `vcu_pwm.c` modules
5. [ ] Bench test commutation before vehicle integration

---

## 📎 References

- [Implementation Plan](../implementation_plan.md) *(in .gemini folder)*
- [Arduino ESC Example](../assests/B-IR2110-DRV-01MBR-V1.0.ino)
- [Architecture Doc](architecture.md)
