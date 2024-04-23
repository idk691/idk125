import time
import random

def hacking_progress():
    print("VPN connection in progress:")
    start_time = time.time()
    error_percentage = random.randint(20, 80)
    for i in range(101):
        if i >= 100:
            i = 100
        print(f"Progress: {i}% ", end="", flush=True)
        remaining_time = 10 - (time.time() - start_time)
        if remaining_time > 0:
            time.sleep(remaining_time / (100 - i))
        if i == error_percentage:
            print("\nError: Connection lost. Reconnecting...")
            time.sleep(2)
            print("Reconnected. Resuming connection...")
        elif i < 30:
            print("[||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||]", end="\r", flush=True)
        elif i < 70:
            print("[||||||||||||||||||||||||||||||||||||||||||||||||||||||          ]", end="\r", flush=True)
        elif i < 90:
            print("[||||||||||||||||||||||||||||||||||||||||||||                    ]", end="\r", flush=True)
        elif i < 99:
            print("[||||||||||||||||||||||||||||||||||||                            ]", end="\r", flush=True)
        else:
            print("[||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||]", end="\r", flush=True)
    print("\nVPN connection successful!")

hacking_progress()
