from typing import List
from src.answers.answer import get_answers_by_id, Answer
from src.questions.question import get_questions, Question
from dataclasses import dataclass
from src.qa.metrics import Metric, get_metrics_from_user_input


@dataclass
class FullQuestion:
    question: Question
    answers: List[Answer]
    metric: Metric




def is_replicant(metric: Metric) -> bool:
    # Примерные границы для человека
    if not (12 <= metric.respiration <= 20):
        return True
    if not (60 <= metric.heart_rate <= 100):
        return True
    if not (1 <= metric.blushing_level <= 3):
        return True
    if not (1 <= metric.pupillary_dilation <= 5):
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


def make_quiz():
    results: List[FullQuestion] = []
    questions = get_questions()

    for q in questions:
        answers = get_answers_by_id(q.id)
        print(q)

        # Ввод номера ответа
        while True:
            for i, a in enumerate(answers, 1):
                print(f"{i}. {a}")

            try:
                selected_answer = int(input("Enter number of answer: ")) - 1
                if selected_answer < 0 or selected_answer >= len(answers):
                    raise IndexError
                chosen_answer = answers[selected_answer]
                break
            except (ValueError, IndexError):
                print("Invalid answer number. Please try again.")

        # Ввод метрики
        while True:
            try:
                metric = get_metrics_from_user_input()
                break
            except ValueError:
                print("Invalid metrics. Please try again.")

        results.append(FullQuestion(q, answers, metric))

    # Определение результата по итогам всего теста
    final_result = determine_result(results)
    print(f"Результат теста: {final_result}")


if __name__ == "__main__":
    make_quiz()