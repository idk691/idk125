import time
import random

def hacking_progress():
    print("Hacking in progress:")
    start_time = time.time()
    for i in range(101):
        print(f"Progress: {i}% ", end="", flush=True)
        remaining_time = 3 - (time.time() - start_time)
        time.sleep(remaining_time / (100 - i) if i < 100 else 0)
        if i < 30:
            print("[||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||]", end="\r", flush=True)
        elif i < 70:
            print("[||||||||||||||||||||||||||||||||||||||||||||||||||||||          ]", end="\r", flush=True)
        elif i < 90:
            print("[||||||||||||||||||||||||||||||||||||||||||||                    ]", end="\r", flush=True)
        elif i < 100:
            print("[||||||||||||||||||||||||||||||||||||                            ]", end="\r", flush=True)
        else:
            print("[||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||]", end="\r", flush=True)
    print("\nHack successful!")

hacking_progress()
