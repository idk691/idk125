import time
import requests

def hacking_progress():
    print("VPN connection in progress:")
    start_time = time.time()
    for i in range(101):
        if i >= 100:
            i = 100
        print(f"Progress: {i}% ", end="", flush=True)
        remaining_time = 10 - (time.time() - start_time)
        if remaining_time > 0:
            time.sleep(remaining_time / (100 - i))
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

status = {
    "Server": "Not Working",
    "Email": "Not Working",
    "Bypass": "Not Working"
}

print("Загрузка страницы: ", end="")
response = requests.get(url)
if response.ok:
    status["Server"] = "Working"
    print("Загрузка страницы: 100% ")
    if 'Ваша электронная почта' in response.text:
        email = input('Введите электронную почту для получения тестового периода: ')
        status["Email"] = "Working"
        print('Email Working')
        response = requests.post('https://hidemy.io/ru/demo/success/', data={"demo_mail": f"{email}"})
        if 'Ваш код выслан на почту' in response.text:
            confirm = input('Введите полученную ссылку для подтверждения e-mail адреса: ')
            while True:
                try:
                    response = requests.get(confirm)
                    if 'Спасибо' in response.text:
                        print('Почта подтверждена. Код отправлен на вашу почту!')
                        status["Bypass"] = "Working"
                        break
                    else:
                        confirm = input('Ссылка невалидная, повторите попытку: ')
                except:
                    confirm = input('Ссылка невалидная, повторите попытку: ')
                    continue
        else:
            print('Указанная почта не подходит для получения тестового периода ')
    else:
        print('Страница не содержит форму для ввода электронной почты')
else:
    print('Ошибка при загрузке страницы')

for key, value in status.items():
    print(f"{key}: {value}")
