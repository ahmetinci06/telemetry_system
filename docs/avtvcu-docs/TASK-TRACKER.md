# AVT VCU Development Task Tracker

> Tracking development progress for TÜBİTAK Efficiency Challenge VCU firmware

---

## 🎯 Current Sprint: Phase 1 - Foundation

**Status:** Sprint 1B Complete ✅

---

## Phase 1: Foundation & Core Systems (Weeks 1-3)

### Sprint 1: Pedal Mapping & ADC ✅ COMPLETE

| Task                                  | Status  | Files               |
| ------------------------------------- | ------- | ------------------- |
| ADC1 configuration (16x oversampling) | ✅ Done | `AVT-VCU-DEV.ioc`   |
| Basic ADC reading                     | ✅ Done | `main.c`            |
| `PedalInput_t` structure              | ✅ Done | `vcu_pedal.h`       |
| Calibration thresholds                | ✅ Done | `vcu_pedal.h/c`     |
| Wire-break detection                  | ✅ Done | `vcu_pedal.c`       |
| Short-circuit detection               | ✅ Done | `vcu_pedal.c`       |
| Low-pass filter                       | ✅ Done | `vcu_pedal.c`       |
| Integration in main.c                 | ✅ Done | `main.c`            |
| Documentation                         | ✅ Done | `docs/vcu_pedal.md` |

**Remaining:**

- [ ] Non-linear efficiency mapping lookup table

---

### Sprint 2: FDCAN Communication ✅ COMPLETE

| Task                       | Status  | Notes                          |
| -------------------------- | ------- | ------------------------------ | --- |
| Configure FDCAN1 in CubeMX | ✅ Done | PA11 RX, PA12 TX               |
| 500 kbit/s bitrate         | ✅ Done | Prescaler=17, Seg1=14, Seg2=5  |
| BMS message parsing        | ✅ Done | 0x100-0x104                    |
| VESC torque command        | ✅ Done | Current control                |
| Timeout detection          | ✅ Done | 500ms BMS, 200ms VESC          |
| Integration in main.c      | ✅ Done | Faults linked to state machine |     |

**Files to create:**

- `Core/Inc/vcu_can.h`
- `Core/Src/vcu_can.c`
- `docs/vcu_can.md`

---

## Phase 2: Energy Management (Weeks 4-6)

### Sprint 3: Energy Monitoring 📋 PLANNED

| Task                                | Status |
| ----------------------------------- | ------ |
| `EnergyMetrics_t` structure         | ⬜     |
| Real-time power calculation (V × I) | ⬜     |
| Energy integration (Wh consumed)    | ⬜     |
| Efficiency calculation (Wh/km)      | ⬜     |

### Sprint 4: Regenerative Braking 📋 PLANNED

| Task                           | Status |
| ------------------------------ | ------ |
| `RegenLevel_t` modes           | ⬜     |
| SOC-based regen limiting       | ⬜     |
| Speed-based regen optimization | ⬜     |

---

## Phase 3: Advanced Control (Weeks 7-9)

### Sprint 5: State Machine ✅ COMPLETE

| Task                                   | Status  | Notes               |
| -------------------------------------- | ------- | ------------------- |
| Vehicle states (OFF/READY/DRIVE/FAULT) | ✅ Done | `vcu_state.h/c`     |
| State transitions with safety checks   | ✅ Done | Request-based       |
| Fault handling and recovery            | ✅ Done | Fault codes defined |
| Integration in main.c                  | ✅ Done | Pedal faults linked |

### Sprint 6: Advanced Strategies 📋 PLANNED

| Task                     | Status |
| ------------------------ | ------ |
| Pulse & Glide controller | ⬜     |
| Predictive speed control | ⬜     |

---

## Phase 4: Telemetry & Driver Assist (Weeks 10-11)

| Task                            | Status |
| ------------------------------- | ------ |
| UART telemetry packet structure | ⬜     |
| Driver coaching system          | ⬜     |
| LoRa/ESP32 wireless integration | ⬜     |

---

## Phase 5: Competition Optimization (Weeks 12-14)

| Task                           | Status |
| ------------------------------ | ------ |
| Race strategy implementation   | ⬜     |
| Auxiliary system management    | ⬜     |
| Fine-tuning for 22.5km / 29min | ⬜     |

---

## Phase 6: Testing & Validation (Weeks 15-16)

| Task                         | Status |
| ---------------------------- | ------ |
| Hardware-in-the-loop testing | ⬜     |
| SD card data logging         | ⬜     |
| Pre-competition checklist    | ⬜     |

---

## 📊 Legend

| Symbol | Meaning     |
| ------ | ----------- |
| ✅     | Complete    |
| 🔄     | In Progress |
| ⬜     | Not Started |
| 📋     | Planned     |
