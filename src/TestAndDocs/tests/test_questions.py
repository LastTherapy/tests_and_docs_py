import pytest
from unittest.mock import patch, mock_open
import json
from src.questions.question import Question, get_questions  # Ваш модуль

# Пример данных для подмены реального JSON-файла
mock_json_data = {
    "questions": [
        {"id": 1, "question": "What is your name?"},
        {"id": 2, "question": "What is your quest?"},
        {"id": 3, "question": "What is your favorite color?"}
    ]
}


def test_question_creation():
    question = Question(1, "What is your name?")

    # Проверяем, что объект создаётся правильно
    assert question.id == 1
    assert question.question == "What is your name?"
    assert str(question) == "Question 1: What is your name?"
    assert repr(question) == "Question 1: What is your name?"


# Тест для функции get_questions с подменой файла JSON
@patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_json_data))
def test_get_questions(mock_file):
    """Тестируем получение вопросов из поддельного JSON"""
    questions = get_questions()

    # Проверяем, что функция вернула правильное количество объектов
    assert len(questions) == 3

    # Проверяем правильность данных в объектах
    assert questions[0].id == 1
    assert questions[0].question == "What is your name?"

    assert questions[1].id == 2
    assert questions[1].question == "What is your quest?"

    assert questions[2].id == 3
    assert questions[2].question == "What is your favorite color?"
