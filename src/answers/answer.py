from typing import List
import json
from pathlib import Path
import random


class Answer:
    def __init__(self, id: int, answer: str):
        self.id = id
        self.answer = answer

    def __str__(self):
        return f'{self.id}: {self.answer}'

    def __repr__(self):
        return f'{self.id}: {self.answer}'


script_dir = Path(__file__).parent
json_file = script_dir / 'answer_list.json'
json_answers = json.load(open(json_file))


def get_answers_by_id(question_id: int) -> List[Answer]:
    answers = []
    for a in json_answers['answers']:
        if a['question_id'] == question_id:
            random.shuffle(a['options'])
            for num, option in enumerate(a['options'], start=1):
                answers.append(Answer(num, option))
    return answers

if __name__ == '__main__':
    print(get_answers_by_id(1))
