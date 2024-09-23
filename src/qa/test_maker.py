from typing import List
from src.answers.answer import get_answers_by_id, Answer
from src.questions.question import get_questions, Question
from dataclasses import dataclass
from metrics import Metric, get_metrics_from_user_input


@dataclass
class FullQuestion:
    question: Question
    answers: List[Answer]
    metric: Metric


def is_replicant(metric: Metric) -> bool:
    # Примерные границы для человека
    if not (12 <= metric.respiraton <= 20):
        return True
    if not (60 <= metric.heart_rate <= 100):
        return True
    if not (1 <= metric.blushing_level <= 3):
        return True
    if not (1 <= metric.pupilary_dilation <= 5):
        return True
    return False


def determine_result(results: List[FullQuestion]) -> str:
    replicant_score = 0
    total_questions = len(results)

    # Считаем количество вопросов, где метрики указывают на репликанта
    for result in results:
        if is_replicant(result.metric):
            replicant_score += 1

    # Если больше половины метрик выходят за рамки, считаем репликантом
    if replicant_score > total_questions / 2:
        return "Репликант"
    else:
        return "Человек"



results: List[FullQuestion] = []
questions = get_questions()

for q in questions:
    answers = get_answers_by_id(q.id)
    print(q)
    for a in answers:
        print(a)
    input("Enter number of answer: ")
    metric = get_metrics_from_user_input()
    results.append(FullQuestion(q, answers, metric))

# Определение результата по итогам всего теста
final_result = determine_result(results)
print(f"Результат теста: {final_result}")
