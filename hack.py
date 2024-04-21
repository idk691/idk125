import time
import random

def hacking_progress():
    print("Hacking in progress:")
    for i in range(101):
        print(f"Progress: {i}% ", end="", flush=True)
        time.sleep(random.uniform(0.05, 0.2))
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
