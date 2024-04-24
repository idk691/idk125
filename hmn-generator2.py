import time
import requests

def hacking_progress():
    print("VPN connection in progress:")
    start_time = time.time()
    for i in range(101):
        if i >= 100:
            i = 100
        print(f"Progress: {i}% ", end="", flush=True)
        time.sleep(0.01)
        if i < 30:
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

url = 'https://hidemy.io/ru/demo/'

response = requests.get(url, timeout=1)
if response.ok:
    print("Загрузка страницы: 100%")
    if 'Ваша электронная почта' in response.text:
        email = input('Введите электронную почту для получения тестового периода: ')
        response = requests.post('https://hidemy.io/ru/demo/success/', data={"demo_mail": f"{email}"}, timeout=1)
        if 'Ваш код выслан на почту' in response.text:
            print('Почта подтверждена. Код отправлен на вашу почту!')
        else:
            print('Указанная почта не подходит для получения тестового периода ')
    else:
        print('Страница не содержит форму для ввода электронной почты')
else:
    print('Ошибка при загрузке страницы')
