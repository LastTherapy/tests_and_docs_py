from typing import List
from src.answers.answer import get_answers_by_id, Answer
from src.questions.question import get_questions, Question
from dataclasses import dataclass
from src.qa.metrics import Metric, get_metrics_from_user_input


@dataclass
class FullQuestion:
    """
    Represents a question, its possible answers, and a user's associated metric.

    Attributes:
        question (Question): The question object.
        answers (List[Answer]): The list of possible answers for the question.
        metric (Metric): The metric data collected from the user.
    """
    question: Question
    answers: List[Answer]
    metric: Metric


def is_replicant(metric: Metric) -> bool:
    """
    Determines if the given metric indicates that the user is a replicant.

    Args:
        metric (Metric): The user's metric data.

    Returns:
        bool: True if the metric data indicates the user is a replicant, otherwise False.

    The criteria used are:
    - Respiration must be between 12 and 20.
    - Heart rate must be between 60 and 100.
    - Blushing level must be between 1 and 3.
    - Pupillary dilation must be between 1 and 5 mm.
    """
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
    """
    Determines whether the user is classified as a replicant or a human based on their metrics.

    Args:
        results (List[FullQuestion]): A list of FullQuestion objects, each containing a question,
                                      a set of possible answers, and the user's metric data.

    Returns:
        str: "Репликант" if the user is classified as a replicant, otherwise "Человек".

    The decision is based on whether more than half of the provided metrics fall outside the human range.
    """
    replicant_score = 0
    total_questions = len(results)

    for result in results:
        if is_replicant(result.metric):
            replicant_score += 1

    if replicant_score > total_questions / 2:
        return "Репликант"
    else:
        return "Человек"


def make_quiz():
    """
    Runs a quiz where the user answers questions and provides associated metrics.

    The quiz consists of:
    1. Displaying each question and possible answers.
    2. Prompting the user to select an answer.
    3. Collecting biological metrics from the user.
    4. Determining whether the user is classified as a replicant or a human based on their metrics.
    """
    results: List[FullQuestion] = []
    questions = get_questions()

    for q in questions:
        answers = get_answers_by_id(q.id)
        print(q)

        # Ввод номера ответа
        while True:
            for i, a in enumerate(answers, 1):
                print(f"{a}")

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
