# ANON-TG-BOT

Простенький бот на python, aiogram.

### Установка / Installation

1. **Клонируем репозиторий:**

``` bash
git clone https://github.com/Microvolna/anon-tg-bot
cd anon-tg-bot
```

2. **Заполняем поля в `.env.dist` и переименовываем его в `.env`**

3. **Устанавливаем зависимости и запускаем бота:**

<details>
<summary>Через uv (рекомендуется)</summary>

**Устанавливаем `uv` (если еще не установлен):**

Linux:

``` bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows:

``` bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Запускаем:**

```bash
uv run bot.py
```

</details>

<details>
<summary>Через requirements.txt</summary>

``` bash
pip install -r requirements.txt
```

> Если вы под Linux-ом не забудьте создать виртуальное окружение
> ``` bash
> python -m venv venv
> . venv/bin/activate
> ```

5. **Запуск бота**
```
python3 bot.py
```
</details>

# Структура проекта

```
.env             - файл с токеном и списком админов
bot.py           - основной файл бота
messages.py      - файл с шаблонами сообщений
requirements.txt - зависимости проекта
```
