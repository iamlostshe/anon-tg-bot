def start_msg(first_name: str, lang_code: str | None = None) -> str:
    return f'''Приветствую, {first_name}!
    
Для того чтобы отправить мне анонимное сообщение просто напиши боту)'''

def success(first_name, lang_code: str | None = None) -> str:
    return f'''Спасибо за вопросик, {first_name})
    
В скором времени постараюсь ответить на него в своем канале!'''

def info(user_id: str, username: str, first_name: str, last_name: str, lang_code: str | None = None):
    return f'''Новое сообщение!
    
Информация об отправителе:

id: {user_id};
username: {username};
first_name: {first_name};
last_name: {last_name};

url (если указан username): https://t.me/{username}

Письмо отправлено отдельным сообщением ниже:
'''
