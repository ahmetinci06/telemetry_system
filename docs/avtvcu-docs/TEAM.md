# 👥 Team & Responsibilities

> AVT VCU Development Team - Area Ownership

---

## 🎯 Quick Reference

| Area                     | Owner      | Status      |
| ------------------------ | ---------- | ----------- |
| **Overall Architecture** | You (Lead) | 🟢 Active   |
| **State Machine**        | Aybüke     | 🟡 Assigned |
| **CAN Bus (BMS/VESC)**   | Ali Efe    | 🟡 Assigned |
| **Pedal Module**         | You (Lead) | ✅ Complete |
| **Energy Monitoring**    | TBD        | ⬜ Open     |
| **Arduino ESC**          | TBD        | ⬜ Open     |
| **Telemetry**            | TBD        | ⬜ Open     |
| **Testing**              | TBD        | ⬜ Open     |

---

## 📋 Detailed Ownership

### 🔄 State Machine - Aybüke

**Files:**

- `Core/Inc/vcu_state.h`
- `Core/Src/vcu_state.c`
- `docs/vcu_state.md`

**Responsibilities:**

- [ ] Review current state machine logic
- [ ] Add pre-charge state if needed
- [ ] Implement startup sequence
- [ ] Test fault transitions
- [ ] Document state diagram

**Notes:**

```
Add your notes here...
```

---

### 📡 CAN Bus - Ali Efe

**Files:**

- `Core/Inc/vcu_can.h`
- `Core/Src/vcu_can.c`
- `docs/vcu_can.md`

**Responsibilities:**

- [ ] Review BMS message format (confirm IDs with BMS team)
- [ ] Test CAN communication with real BMS
- [ ] Implement VESC status parsing
- [ ] Add CAN error handling
- [ ] Document actual message formats

**Notes:**

```
Add your notes here...
```

---

### 🎛️ Pedal Module - Lead (You)

**Files:**

- `Core/Inc/vcu_pedal.h`
- `Core/Src/vcu_pedal.c`
- `docs/vcu_pedal.md`

**Status:** ✅ Complete

**Completed Tasks:**

- [x] ADC reading with oversampling
- [x] Low-pass filter
- [x] Wire-break detection
- [x] Short-circuit detection
- [x] Calibration support

---

### ⚡ Energy Monitoring - TBD

**Files (to be created):**

- `Core/Inc/vcu_energy.h`
- `Core/Src/vcu_energy.c`
- `docs/vcu_energy.md`

**Responsibilities:**

- [ ] Wh consumption tracking
- [ ] Wh/km efficiency calculation
- [ ] Regeneration tracking
- [ ] Range estimation

**To assign, add name above and start working!**

---

### 🔌 Arduino ESC - TBD

**Files:**

- `docs/arduino-esc.md` (reference)
- `Core/Inc/vcu_esc.h` (to be created)
- `Core/Src/vcu_esc.c` (to be created)

**Responsibilities:**

- [ ] UART communication with Arduino
- [ ] Command protocol implementation
- [ ] Timeout/fault handling
- [ ] Arduino firmware development

---

### 📊 Telemetry - TBD

**Files (to be created):**

- `Core/Inc/vcu_telemetry.h`
- `Core/Src/vcu_telemetry.c`

**Responsibilities:**

- [ ] UART/Bluetooth data output
- [ ] Log format design
- [ ] Real-time monitoring app

---

## 🏗️ Overall - Lead (You)

**Responsibilities:**

- `main.c` integration
- Code review
- Architecture decisions
- CubeMX configuration
- Build system
- Documentation structure

---

## 📝 How to Update This Document

1. **Claim an area:** Add your name to the "TBD" spots
2. **Update status:** Change status emoji (⬜ → 🟡 → 🟢 → ✅)
3. **Check off tasks:** Mark `[ ]` as `[x]` when done
4. **Add notes:** Use the notes section for important info
5. **Commit changes:** `git commit -m "docs: Update team assignments"`

---

## 📅 Status Legend

| Emoji | Meaning                     |
| ----- | --------------------------- |
| ⬜    | Open - Not assigned         |
| 🟡    | Assigned - Work not started |
| 🟢    | Active - In progress        |
| ✅    | Complete                    |
| 🔴    | Blocked                     |

---

## 📞 Contact

| Name    | Role          | Contact |
| ------- | ------------- | ------- |
| Lead    | Project Lead  | -       |
| Aybüke  | State Machine | -       |
| Ali Efe | CAN Bus       | -       |

_Add contact info as needed_

---

**Last Updated:** 2024-12-24
