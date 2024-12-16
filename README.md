# ANON-TG-BOT

Простенький бот на python, aiogram.

### Установка / Installation

1. **Клонируем репозиторий:**

``` bash
git clone https://github.com/Microvolna/ANON-TG-BOT
```

2. **Переходим в дирректорию с проектом:**

``` bash
cd ANON-TG-BOT
```

3. **Устанавливаем необходимые зависимости:**

``` bash
pip install -r requirements.txt
```

> Если вы под Linux-ом не забудьте создать виртуальное окружение
> ``` bash
> python -m venv venv
> . venv/bin/activate
> ```

4. **Заполняем поля в `.env.dist` и переименовываем его в `.env`**

5. **Запуск бота**
```
python3 bot.py
```

# Структура проекта

```
.env             - файл с токеном и списком админов
bot.py           - основной файл бота
messages.py      - файл с шаблонами сообщений
requirements.txt - зависимости проекта
```
