import requests
import random
import string

# Генерация случайного ID
random_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

url = f'https://hidemy.io/ru/demo/{random_id}/'

if 'Ваша электронная почта' in requests.get(url).text:
    
    email = input('Введите электронную почту для получения тестового периода: ')

    response = requests.post(f'https://hidemy.io/ru/demo/{random_id}/success/', data={
        "demo_mail": f"{email}"
    })

    if 'Ваш код выслан на почту' in response.text:
        confirm = input('Введите полученную ссылку для подтверждения e-mail адреса: ')
        
        while True:
            try:
                response = requests.get(confirm)
                if 'Спасибо' in response.text:
                    print('Почта подтверждена. Код отправлен на вашу почту!')
                    break
                else:
                    confirm = input('Ссылка невалидная, повторите попытку: ')
            except:
                confirm = input('Ссылка невалидная, повторите попытку: ')
                continue


    else:
        print('Указанная почта не подходит для получения тестового периода ')

else:
    print('Невозможно получить тестовый период')
