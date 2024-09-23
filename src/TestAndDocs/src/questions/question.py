from typing import List
import json
from pathlib import Path


class Question:
    def __init__(self, id: int, question: str):
        self.id = id
        self.question = question

    def __str__(self):
        return f'Question {self.id}: {self.question}'

    def __repr__(self):
        return f'Question {self.id}: {self.question}'


def get_questions() -> List[Question]:
    questions: List = []
    script_dir = Path(__file__).parent
    json_file = script_dir / 'question_list.json'
    json_questions = json.load(open(json_file))

    for q in json_questions['questions']:
        questions.append(Question(q['id'], q['question']))
    return questions
