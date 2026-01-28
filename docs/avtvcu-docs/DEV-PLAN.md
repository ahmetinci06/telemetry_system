Looking at your development plan and the TÜBİTAK Efficiency Challenge requirements for the Elektromobil category, here's a comprehensive software roadmap for AVT's VCU development:

# AVT VCU Software Development Roadmap for Efficiency Competitions

## 🎯 Competition-Specific Requirements (Elektromobil Category)
- **Energy Limit**: 3kWh battery capacity max
- **Distance**: 22.5 km in 29 minutes (avg ~46.5 km/h)
- **Scoring**: Based on Wh/km efficiency
- **Critical Factor**: Every 0.1 Wh/km improvement matters

## 📊 Phase 1: Foundation & Core Systems (Weeks 1-3)
*Aligns with your Sprint 1-2*

### 1.1 Enhanced Pedal Mapping with Efficiency Curves
```c
typedef struct {
    float pedal_position;     // 0-100%
    float motor_efficiency;   // Current operating efficiency
    float optimal_torque;     // Calculated from MTPA
    float battery_soc;       // State of charge
    float temperature_derating; // Temperature-based power limit
} PedalMapping_t;

// Implement non-linear mapping for efficiency
float calculate_efficient_torque(PedalMapping_t* map) {
    // Use lookup table from motor dyno data
    // Apply efficiency map (typically 85-95% efficient zones)
    return optimized_torque;
}
```

### 1.2 FDCAN Implementation with Priority Messaging
- **High Priority (1ms)**: Safety signals, emergency stop
- **Medium Priority (10ms)**: Torque commands, state transitions  
- **Low Priority (100ms)**: Telemetry, non-critical data

```c
// FDCAN configuration for STM32G4
FDCAN_FilterTypeDef sFilterConfig;
sFilterConfig.IdType = FDCAN_EXTENDED_ID;
sFilterConfig.FilterIndex = 0;
sFilterConfig.FilterType = FDCAN_FILTER_MASK;
sFilterConfig.FilterConfig = FDCAN_FILTER_TO_RXFIFO0;
sFilterConfig.FilterID1 = 0x100;  // BMS messages
sFilterConfig.FilterID2 = 0x200;  // VESC messages
```

## 📊 Phase 2: Energy Management System (Weeks 4-6)
*Extends Sprint 3-4*

### 2.1 Real-Time Energy Monitoring
```c
typedef struct {
    float instant_power_w;        // V * I
    float energy_consumed_wh;     // Integrated over time
    float distance_traveled_km;   // From wheel encoder
    float efficiency_whkm;        // Real-time efficiency
    float projected_range_km;     // Based on current consumption
    float optimal_speed_kmh;      // For current conditions
} EnergyMetrics_t;

// Update every 100ms
void update_energy_metrics(EnergyMetrics_t* metrics) {
    metrics->instant_power_w = battery_voltage * battery_current;
    metrics->energy_consumed_wh += (metrics->instant_power_w * 0.1) / 3600;
    metrics->efficiency_whkm = metrics->energy_consumed_wh / metrics->distance_traveled_km;
}
```

### 2.2 Regenerative Braking Optimization
```c
typedef enum {
    REGEN_OFF = 0,
    REGEN_LIGHT = 20,    // 20% recovery
    REGEN_MEDIUM = 40,    // 40% recovery
    REGEN_HEAVY = 60,     // 60% recovery
    REGEN_ADAPTIVE = 100  // Dynamic based on conditions
} RegenLevel_t;

float calculate_regen_current(float vehicle_speed, float battery_soc) {
    if (battery_soc > 95.0f) return 0;  // Prevent overcharge
    if (vehicle_speed < 10.0f) return 0; // Too slow for efficient regen
    
    // Optimal regen between 20-50 km/h
    float regen_efficiency = map_range(vehicle_speed, 20, 50, 0.7, 0.95);
    return MAX_REGEN_CURRENT * regen_efficiency;
}
```

## 📊 Phase 3: Advanced Control Algorithms (Weeks 7-9)

### 3.1 Pulse & Glide Strategy Implementation
```c
typedef struct {
    float target_speed;
    float pulse_threshold_high;  // Start pulse
    float glide_threshold_low;   // End glide
    float optimal_acceleration;  // Most efficient acceleration rate
    uint32_t glide_duration_ms;
    uint32_t pulse_duration_ms;
} PulseGlideParams_t;

void pulse_glide_controller(PulseGlideParams_t* params) {
    static enum {PULSE, GLIDE} state = GLIDE;
    
    switch(state) {
        case GLIDE:
            set_torque_command(0);  // Coast
            if (vehicle_speed < params->glide_threshold_low) {
                state = PULSE;
            }
            break;
            
        case PULSE:
            set_torque_command(params->optimal_acceleration);
            if (vehicle_speed > params->pulse_threshold_high) {
                state = GLIDE;
            }
            break;
    }
}
```

### 3.2 Predictive Speed Control
```c
// Track profile data (from practice runs)
typedef struct {
    float distance_m;
    float elevation_m;
    float optimal_speed_kmh;
    float curve_radius_m;
} TrackSegment_t;

// Predict optimal speed for next segment
float get_optimal_speed(float current_position, TrackSegment_t* track_data) {
    // Look ahead 100-200m
    // Account for elevation changes
    // Reduce speed before curves, accelerate after
    return calculated_optimal_speed;
}
```

## 📊 Phase 4: Telemetry & Driver Assistance (Weeks 10-11)
*Enhances Sprint 5*

### 4.1 Driver Efficiency Coaching System
```c
typedef struct {
    float efficiency_score;      // 0-100%
    char coaching_message[64];   // Real-time tips
    float target_speed;          // Optimal for current segment
    float coast_countdown;       // Time to start coasting
    uint8_t led_pattern;        // Visual feedback (RGB LED)
} DriverCoaching_t;

void update_coaching(DriverCoaching_t* coach) {
    if (throttle_position > 70 && vehicle_speed > 45) {
        strcpy(coach->coaching_message, "EASE OFF - Entering inefficient zone");
        coach->led_pattern = LED_YELLOW_FLASH;
    }
    // More coaching logic...
}
```

### 4.2 Wireless Telemetry with LoRa/ESP32
```c
// Optimized packet structure (minimize transmission power)
typedef struct __attribute__((packed)) {
    uint16_t speed_kmh_x10;      // Speed * 10 (0.1 km/h resolution)
    uint16_t power_w;            // Current power draw
    uint16_t efficiency_whkm_x10; // Efficiency * 10
    uint16_t battery_voltage_x10; // Voltage * 10
    int16_t battery_current_x10;  // Current * 10 (signed)
    uint8_t vehicle_state;       // State machine status
    uint8_t fault_flags;         // Compressed fault info
    uint8_t soc_percent;         // Battery SOC
} TelemetryPacket_t;  // Total: 15 bytes
```

## 📊 Phase 5: Competition-Specific Optimizations (Weeks 12-14)

### 5.1 TÜBİTAK Efficiency Challenge Specific
```c
// Race strategy for 22.5km in 29 minutes
typedef struct {
    float energy_budget_wh;      // Total energy allocation
    float checkpoint_targets[5]; // Energy targets at 5km intervals
    float weather_compensation;  // Wind/temperature factors
} RaceStrategy_t;

void initialize_race_strategy(RaceStrategy_t* strategy) {
    strategy->energy_budget_wh = 2800;  // Leave margin from 3kWh
    // Distribute energy: more for acceleration, less for cruising
    strategy->checkpoint_targets[0] = 600;  // First 5km
    strategy->checkpoint_targets[1] = 550;  // 5-10km
    strategy->checkpoint_targets[2] = 550;  // 10-15km
    strategy->checkpoint_targets[3] = 550;  // 15-20km
    strategy->checkpoint_targets[4] = 550;  // Final 2.5km
}
```

### 5.2 Auxiliary System Management
```c
// Minimize parasitic losses
typedef struct {
    bool cooling_fan_enable;
    uint8_t fan_speed_percent;
    bool telemetry_enable;
    uint8_t telemetry_rate_hz;
    bool lights_enable;
} AuxiliaryControl_t;

void optimize_auxiliary_systems(AuxiliaryControl_t* aux, float motor_temp) {
    // Only cool when necessary
    if (motor_temp < 60.0f) {
        aux->cooling_fan_enable = false;
    } else if (motor_temp > 70.0f) {
        aux->cooling_fan_enable = true;
        aux->fan_speed_percent = map_range(motor_temp, 70, 90, 30, 100);
    }
    
    // Reduce telemetry rate when battery is low
    if (battery_soc < 20.0f) {
        aux->telemetry_rate_hz = 1;  // Minimal updates
    }
}
```

## 📊 Phase 6: Testing & Validation (Weeks 15-16)
*Extends Sprint 6*

### 6.1 Hardware-in-the-Loop Testing
```c
// Simulate race conditions
void run_hil_test(uint8_t test_scenario) {
    switch(test_scenario) {
        case TEST_EFFICIENCY_RUN:
            simulate_track_conditions();
            log_energy_consumption();
            break;
        case TEST_REGEN_BRAKING:
            test_regen_at_various_speeds();
            break;
        case TEST_FAULT_HANDLING:
            inject_fault_conditions();
            verify_safety_response();
            break;
    }
}
```

### 6.2 Data Logging & Analysis
```c
// High-resolution logging for post-race analysis
typedef struct {
    uint32_t timestamp_ms;
    float gps_lat, gps_lon;
    float speed_kmh;
    float motor_rpm;
    float battery_voltage;
    float battery_current;
    float motor_temp;
    float controller_temp;
    float efficiency_instant;
    uint8_t throttle_position;
    uint8_t brake_position;
} BlackBoxData_t;

// Log to SD card via SPI
void log_to_sd_card(BlackBoxData_t* data) {
    // Write binary data for space efficiency
    // Include CRC for data integrity
}
```

## 🎯 Key Performance Indicators (KPIs)

### Software Performance Targets:
- **Main Loop Frequency**: ≥1000 Hz
- **CAN Message Latency**: <1ms for critical messages
- **ADC Sampling Rate**: ≥10 kHz for pedal input
- **State Machine Transition**: <10ms
- **Telemetry Update Rate**: 10-50 Hz adaptive

### Energy Efficiency Targets:
- **Overall Efficiency**: >85% battery-to-wheel
- **Regeneration Recovery**: >15% of total energy
- **Auxiliary Power**: <50W average
- **Idle Power**: <10W
- **Target Consumption**: <130 Wh/km (for winning performance)

## 🛠 Development Tools & Setup

### Required Hardware:
- NUCLEO-G491RE Development Board
- CAN Transceiver (MCP2551/TJA1050)
- Current Sensor (ACS712 or similar)
- GPS Module (for precise distance/speed)
- SD Card Module (for data logging)
- LoRa/ESP32 for telemetry

### Software Stack:
```
STM32CubeIDE → Development Environment
├── HAL/LL Drivers → Hardware abstraction
├── FreeRTOS → Real-time scheduling
├── VESC Tool → Motor configuration
├── Python Scripts → Data analysis
└── MATLAB/Simulink → Control algorithm simulation
```

### Version Control Strategy:
```bash
main
├── develop
│   ├── feature/pedal-mapping
│   ├── feature/can-communication
│   ├── feature/energy-monitor
│   └── feature/telemetry
└── release/v1.0-competition
```

## 📈 Continuous Improvement Process

### Weekly Milestones:
1. **Monday**: Code review & merge features
2. **Wednesday**: Track testing (if available)
3. **Friday**: Data analysis & optimization
4. **Weekend**: Algorithm refinement

### Pre-Competition Checklist:
- [ ] All safety features tested
- [ ] Energy consumption validated <130 Wh/km
- [ ] Telemetry streaming stable
- [ ] Backup VCU programmed
- [ ] Race strategy configured
- [ ] Driver coaching system calibrated
- [ ] Data logging verified
- [ ] Fault recovery tested

## 🚀 Next Steps

1. **Immediate**: Complete Sprint 1 (ADC reading) with efficiency-focused mapping
2. **This Week**: Set up FDCAN with proper message priorities
3. **Next Week**: Implement basic energy monitoring
4. **Testing**: Schedule dyno time for motor characterization
5. **Documentation**: Create driver manual with efficiency tips

Remember: In efficiency competitions, **every single Wh/km counts**. The difference between 1st and 10th place might be just 5-10 Wh/km. Focus on:
- Minimizing losses at every level
- Optimizing for the most common operating points
- Testing, measuring, and iterating constantly

Good luck with the development! Let me know if you need specific implementation details for any component, especially the FDCAN setup on STM32G4 or the energy optimization algorithms.
