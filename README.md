## Шаблон бота с chatgpt4

для начала клонируем или скачиваем этот проект zip архивом.

>git clone https://github.com/Vinifeju/chgptbot

Устанавливаем либы из requirements

> pip3 install -r .\requirements.txt

Устанавливаем токен бота в переменную окружения BOT_TOKEN. 
и раскомментируем строку `#BOT_TOKEN = environ.get('BOT_TOKEN')`

Можно и в коде, но небезопасно

**Прокси**
прокси можем устанавливать в строке `chatgptrequest = ChatGptRequests(proxy={})` в аргументе proxy
в таком же формате как и в requests: {'http': 'http://<host>:<port>'} или socks

Запускаем main.py

/say - запрос к chatgpt

![image](https://i.ibb.co.com/Qvrdnbp/2024-03-05-155527.png)

