import time
import random
import sys
import os

# Target log path monitored by our Wazuh agent pipeline
LOG_PATH = "/var/log/starforce_noise.log"

sources = ["192.168.1.50", "10.0.0.15", "172.16.4.22", "192.168.100.88"]
noise_types = ["port_scan", "packet_storm", "brute_force", "rogue_beacon", "wave_desync"]

def generate_noise():
    print(f"[*] Initializing StarForce Noise Injector -> Writing to {LOG_PATH}")
    print("[*] Press Ctrl+C to halt noise emission.\n")
    
    try:
        while True:
            srcip = random.choice(sources)
            ntype = random.choice(noise_types)
            score = random.randint(15, 35)
            
            log_line = f"NOISE_EVENT srcip={srcip} type={ntype} score={score}"
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            formatted_entry = f"{timestamp} - {log_line}\n"
            
            print(f"[EM-WAVE EMISSION] {log_line}")
            
            # Append to the simulated log file
            with open(LOG_PATH, "a") as f:
                f.write(formatted_entry)
                
            # Random pulse interval between 1 to 3 seconds
            time.sleep(random.uniform(1.0, 3.0))
            
    except KeyboardInterrupt:
        print("\n[!] Noise injection halted. Wave-Road stabilizing.")
        sys.exit(0)

if __name__ == "__main__":
    generate_noise()
