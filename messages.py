"""Модуль статических заготовленных сообщений."""

from __future__ import annotations


def select_lang(lang_code: str | None) -> str:
    """Вспомогательная функция; определяет язык ответа."""
    # Определяем язык ответа
    if not lang_code:
        return "ru"

    return "ru" if lang_code == "ru" else "en"


def start_msg(first_name: str, lang_code: str | None = None) -> str:
    """Ответ на приветственное сообщение."""
    # Возвращаем текст ответа
    return {
        "ru": (
            f"Приветствую, {first_name}!\n\n"
            "Для того чтобы отправить мне анонимное сообщение просто напиши боту)"
        ),
        "en": (
            f"Hello, {first_name}!\n\n."
            "To send me an anonymous message, just message the bot."
        ),
    }[select_lang(lang_code)]

def success(first_name: str, lang_code: str | None = None) -> str:
    """Ответ на сообщение-анонимный вопрос."""
    # Возвращаем текст ответа
    return {
        "ru": (
            f"Спасибо за вопросик, {first_name})\n\n"
            "В скором времени постараюсь ответить на него!"  # noqa: RUF001
        ),
        "en": (
            "Thank you for the question, {first_name})\n\n"
            "I'll try to answer it soon!"
        ),
    }[select_lang(lang_code)]
