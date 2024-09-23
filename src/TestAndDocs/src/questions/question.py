from typing import List
import json
from pathlib import Path


class Question:
    """
    Represents a question with an ID and question text.

    Attributes:
        id (int): The identifier for the question.
        question (str): The text of the question.
    """

    def __init__(self, id: int, question: str):
        """
        Initializes a Question object.

        Args:
            id (int): The identifier for the question.
            question (str): The text of the question.
        """
        self.id = id
        self.question = question

    def __str__(self):
        """
        Returns a string representation of the Question object.

        Returns:
            str: The string representation in the format 'Question id: question'.
        """
        return f'Question {self.id}: {self.question}'

    def __repr__(self):
        """
        Returns the official string representation of the Question object.

        Returns:
            str: The string representation in the format 'Question id: question'.
        """
        return f'Question {self.id}: {self.question}'


def get_questions() -> List[Question]:
    """
    Retrieves a list of questions from a JSON file.

    Reads a JSON file 'question_list.json', parses it, and returns
    a list of Question objects.

    Returns:
        List[Question]: A list of Question objects retrieved from the JSON file.
    """
    questions: List[Question] = []
    script_dir = Path(__file__).parent
    json_file = script_dir / 'question_list.json'
    json_questions = json.load(open(json_file))

    for q in json_questions['questions']:
        questions.append(Question(q['id'], q['question']))
    return questions
