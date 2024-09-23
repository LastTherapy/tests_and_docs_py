import pytest
from typing import List
from unittest.mock import patch
import random
from src.answers.answer import Answer, get_answers_by_id




mock_json_data = {
    "answers": [
        {
            "question_id": 1,
            "options": ["Answer 1", "Answer 2", "Answer 3", "Answer 4"]
        },
        {
            "question_id": 2,
            "options": ["Option A", "Option B", "Option C"]
        }
    ]
}

@patch('src.answers.answer.json_answers', mock_json_data)  # Путь к переменной json_answers
def test_get_answers_by_id():
    """Тестирует получение ответов для вопроса с ID 1"""
    answers = get_answers_by_id(1)

    # Проверяем, что вернулось 4 ответа
    assert len(answers) == 4

    # Проверяем, что ответы содержат корректные данные
    expected_answers = ["Answer 1", "Answer 2", "Answer 3", "Answer 4"]
    result_answers = [answer.answer for answer in answers]

    # Порядок должен быть случайным, но все элементы должны присутствовать
    assert sorted(expected_answers) == sorted(result_answers)


@patch('src.answers.answer.json_answers', mock_json_data)  # Путь к переменной json_answers
def test_get_answers_by_id_with_different_id():
    """Тестирует получение ответов для вопроса с ID 2"""
    answers = get_answers_by_id(2)

    # Проверяем, что вернулось 3 ответа
    assert len(answers) == 3

    # Проверяем, что ответы содержат корректные данные
    expected_answers = ["Option A", "Option B", "Option C"]
    result_answers = [answer.answer for answer in answers]

    # Порядок должен быть случайным, но все элементы должны присутствовать
    assert sorted(expected_answers) == sorted(result_answers)


@patch('src.answers.answer.json_answers', mock_json_data)  # Путь к переменной json_answers
def test_get_answers_by_id_empty():
    """Тестирует случай с несуществующим вопросом"""
    answers = get_answers_by_id(999)

    # Проверяем, что для несуществующего вопроса возвращается пустой список
    assert answers == []
