import sys
import time

def loading_animation(duration):
    while duration > 0:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)
        duration -= 1

print("Подключение к серверу", end="")
loading_animation(10)
print("\nНе удалось подключить к серверу")
