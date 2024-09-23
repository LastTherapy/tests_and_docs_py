from typing import List
import json
from pathlib import Path
import random


class Answer:
    """
    Represents an answer for a question.

    Attributes:
        id (int): The identifier for the answer.
        answer (str): The text of the answer.
    """

    def __init__(self, id: int, answer: str):
        """
        Initializes an Answer object.

        Args:
            id (int): The identifier for the answer.
            answer (str): The text of the answer.
        """
        self.id = id
        self.answer = answer

    def __str__(self):
        """
        Returns a string representation of the Answer object.

        Returns:
            str: The string representation in the format 'id: answer'.
        """
        return f'{self.id}: {self.answer}'

    def __repr__(self):
        """
        Returns the official string representation of the Answer object.

        Returns:
            str: The string representation in the format 'id: answer'.
        """
        return f'{self.id}: {self.answer}'


script_dir = Path(__file__).parent
json_file = script_dir / 'answer_list.json'
json_answers = json.load(open(json_file))


def get_answers_by_id(question_id: int) -> List[Answer]:
    """
    Retrieves and shuffles the list of answers for a given question ID.

    Args:
        question_id (int): The ID of the question for which answers are retrieved.

    Returns:
        List[Answer]: A list of Answer objects for the specified question, with options shuffled.
    """
    answers = []
    for a in json_answers['answers']:
        if a['question_id'] == question_id:
            random.shuffle(a['options'])
            for num, option in enumerate(a['options'], start=1):
                answers.append(Answer(num, option))
    return answers


if __name__ == '__main__':
    print(get_answers_by_id(1))
