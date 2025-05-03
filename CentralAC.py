import random
import time

class GreenBrainAI:
    def __init__(self):
        self.energy_usage = 0  # in megawatts
        self.air_quality_index = 50  # AQI scale (0-500)
        self.traffic_congestion = 20  # percentage
        self.green_energy_ratio = 0.45  # % of green energy used

    def monitor_environment(self):
        self.air_quality_index = random.randint(20, 150)
        print(f"[Environment] Current Air Quality Index: {self.air_quality_index}")
        if self.air_quality_index > 100:
            print("[Alert] Poor air quality! Activating air purification systems.")

    def manage_traffic(self):
        self.traffic_congestion = random.randint(10, 80)
        print(f"[Traffic] Current congestion level: {self.traffic_congestion}%")
        if self.traffic_congestion > 60:
            print("[Traffic AI] Rerouting traffic to reduce congestion.")

    def optimize_energy_usage(self):
        self.energy_usage = random.uniform(50.0, 200.0)
        self.green_energy_ratio = random.uniform(0.3, 0.9)
        print(f"[Energy] Current usage: {self.energy_usage:.2f} MW")
        print(f"[Energy] Green energy ratio: {self.green_energy_ratio:.2%}")
        if self.green_energy_ratio < 0.5:
            print("[Energy AI] Increasing solar and wind intake...")

    def city_report(self):
        print("\n--- GREEN BRAIN CITY REPORT ---")
        self.monitor_environment()
        self.manage_traffic()
        self.optimize_energy_usage()
        print("--- END OF REPORT ---\n")


# Simulate the AI system
green_brain = GreenBrainAI()

# Run the system every 10 seconds (for demonstration, we'll run it 3 times)
for _ in range(3):
    green_brain.city_report()
    time.sleep(2)  # simulate delay
