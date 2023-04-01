import os
import json
from string import ascii_uppercase


class AddQuestions:

    def __init__(self, path_file):
        self.path_file = path_file
        self.question: dict = {}
        self.questions: list = []

    def new_question(self, question: str, answers: dict) -> None:
        id_q = 1 if len(self.questions) <= 0 else len(self.questions) + 1
        self.question = {"id": id_q,
                         "question": question,
                         "answers": answers
                         }
        self.questions.append(self.question)

    def add_answers(self) -> dict:
        answers: dict = {}
        for char in range(4):
            answer = input(f"Wprowadź odpowiedź {ascii_uppercase[char]} :").capitalize()
            answers[ascii_uppercase[char]] = [answer, False]
        answers[input("Poprawna odpowiedź: ").upper()][1] = True
    
        return answers

    def __enter__(self):
        try:
            if os.path.isfile(self.path_file):
                with open(self.path_file, "r", encoding="utf-8") as file:
                    data = json.load(file)
                self.questions.extend(data)
        except:
            pass
        return self

    def __exit__(self, exp_typ, exp_val, exp_tb):
        try:
            with open(self.path_file, "w", encoding="utf-8") as file:
                data = json.dumps(self.questions, ensure_ascii=False)
                file.write(data)
        except:
            pass



if __name__ == "__main__":
    with AddQuestions("questions.json") as ad:

        ad.new_question(input("Wprowadź pytanie: ").capitalize(), ad.add_answers())
    