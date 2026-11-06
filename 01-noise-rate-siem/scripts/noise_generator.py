import time
import random
import sys

sources = ["192.168.1.50", "10.0.0.15", "172.16.4.22"]
noise_types = ["port_scan", "brute_force", "packet_storm", "rogue_beacon"]

print("[*] Initializing StarForce Noise Injector... Press Ctrl+C to stop.")
try:
    while True:
        srcip = random.choice(sources)
        ntype = random.choice(noise_types)
        score = random.randint(15, 30)
        
        log_line = f"NOISE_EVENT srcip={srcip} type={ntype} score={score}"
        print(f"[EM-WAVE EMISSION] {log_line}")
        
        # Append to a local log file monitored by Wazuh agent if desired
        with open("/var/log/noise_sim.log", "a") as f:
            f.write(log_line + "\n")
            
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[*] Noise injection halted. System stabilizing.")
    sys.exit(0)
