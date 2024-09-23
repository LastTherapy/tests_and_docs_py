import unittest
from unittest.mock import patch
from pydantic import ValidationError
from src.qa.quiz_maker import FullQuestion, determine_result, make_quiz
from src.questions.question import Question
from src.answers.answer import Answer
from src.qa.metrics import Metric
import pytest
from io import StringIO
import sys

class TestQuizMaker(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '14', '80', '3', '4'])  # Подменяем ввод для ответа и метрики
    @patch('src.qa.quiz_maker.get_answers_by_id', return_value=[Answer(id=1, answer="Answer 1"), Answer(id=2, answer="Answer 2")])  # Подменяем ответы
    @patch('src.qa.quiz_maker.get_questions', return_value=[Question(id=1, question="Question 1")])  # Подменяем список вопросов
    @patch('src.qa.quiz_maker.get_metrics_from_user_input', return_value=Metric(respiration=14, heart_rate=80, blushing_level=3, pupillary_dilation=4))  # Подменяем метрики
    def test_make_quiz_valid_input(self, mock_get_questions, mock_get_answers, mock_get_metrics, mock_input):
        # Тестируем функцию make_quiz, которая использует пользовательский ввод
        make_quiz()  # Запуск теста

    @patch('builtins.input', side_effect=['1', '10', '150', '7', '9', '14', '80', '3', '4'])
    @patch('src.qa.quiz_maker.get_answers_by_id', return_value=[Answer(id=1, answer="Answer 1"), Answer(id=2, answer="Answer 2")])
    @patch('src.qa.quiz_maker.get_questions', return_value=[Question(id=1, question="Question 1")])
    def test_make_quiz_invalid_metrics(self, mock_get_questions, mock_get_answers, mock_input):
        # Захват stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            make_quiz()
        finally:
            # Вернуть stdout на место, даже если произошла ошибка
            sys.stdout = sys.__stdout__

        # Получить вывод и сделать проверку
        output = captured_output.getvalue()
        self.assertIn("Invalid metrics. Please try again.", output)
        self.assertIn("Результат теста: Человек", output)

    @patch('builtins.input', side_effect=['1', '3', '14', '80', '3', '4'])  # Подменяем ввод с ошибкой для ответа
    @patch('src.qa.quiz_maker.get_answers_by_id', return_value=[Answer(id=1, answer="Answer 1"), Answer(id=2, answer="Answer 2")])  # Подменяем ответы
    @patch('src.qa.quiz_maker.get_questions', return_value=[Question(id=1, question="Question 1")])  # Подменяем список вопросов
    @patch('src.qa.quiz_maker.get_metrics_from_user_input', return_value=Metric(respiration=14, heart_rate=80, blushing_level=3, pupillary_dilation=4))  # Подменяем метрики
    def test_make_quiz_invalid_answer(self, mock_get_questions, mock_get_answers, mock_get_metrics, mock_input):
        # Тестируем ввод с ошибкой в ответах
        make_quiz()

    def test_determine_result_replicant(self):
        # Тест на результат "Репликант"
        results = [
            FullQuestion(
                question=Question(id=1, question="Question 1"),
                answers=[Answer(id=1, answer="Answer 1")],
                metric=Metric(respiration=12, heart_rate=100, blushing_level=6, pupillary_dilation=8)
                # Корректные значения
            ),
            FullQuestion(
                question=Question(id=2, question="Question 2"),
                answers=[Answer(id=2, answer="Answer 2")],
                metric=Metric(respiration=13, heart_rate=99, blushing_level=5, pupillary_dilation=7)
                # Корректные значения
            )
        ]
        result = determine_result(results)
        self.assertEqual(result, "Репликант")

    def test_determine_result_human(self):
        # Тест на результат "Человек"
        results = [
            FullQuestion(
                question=Question(id=1, question="Question 1"),
                answers=[Answer(id=1, answer="Answer 1")],
                metric=Metric(respiration=14, heart_rate=80, blushing_level=3, pupillary_dilation=4)
            ),
            FullQuestion(
                question=Question(id=2, question="Question 2"),
                answers=[Answer(id=2, answer="Answer 2")],
                metric=Metric(respiration=15, heart_rate=70, blushing_level=2, pupillary_dilation=3)
            )
        ]
        result = determine_result(results)
        self.assertEqual(result, "Человек")


if __name__ == '__main__':
    unittest.main()
