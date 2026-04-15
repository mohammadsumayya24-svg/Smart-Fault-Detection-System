# Smart Fault Detection System (Simulation-Based Project)

import random
import time

print("🔧 Smart Fault Detection System Started...\n")

while True:
    # Simulated sensor values
    temperature = random.randint(50, 100)   # in °C
    vibration = random.randint(1, 10)       # vibration level
    current = random.randint(5, 20)         # in Amps

    print("📊 Sensor Readings:")
    print(f"Temperature: {temperature} °C")
    print(f"Vibration: {vibration}")
    print(f"Current: {current} A")

    # Fault detection logic
    if temperature > 75:
        print("⚠️ Fault: Motor Overheating Detected")

    if vibration > 6:
        print("⚠️ Fault: Mechanical Issue Detected")

    if current > 15:
        print("⚠️ Fault: Electrical Overload Detected")

    if temperature <= 75 and vibration <= 6 and current <= 15:
        print("✅ System is Working Normally")

    print("-" * 40)

    time.sleep(1)   # delay for 3 seconds