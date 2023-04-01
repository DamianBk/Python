import json


class Questions:

    def __init__(self, id_question: int, question: str, answers: str):
        self._id_question = id_question
        self._question = question
        self._answers = answers

    
    def _is_correct(self, user_answer: str):
        return self._answers[user_answer][1]  # type:ignore


    @property
    def show_question(self):
        out_answers = f"Odpowiedzi:\n"
        for answer in self._answers:

            out_answers += f"{answer}) {self._answers[answer][0]}\n"  # type:ignore

        print(f"Pytanie {self._id_question}: {self._question}\n{out_answers}")


class LoadQuestions:
    def __init__(self, path_file):
        self.__path_file = path_file
        self.questions = []

    def _load_questions(self):
        try:
            with open(self.__path_file, encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, FileExistsError) as error:
            print(f"Podany plik nie istnieje {self.__path_file}, {error}")
        else:
            return [Questions(
                    id_question=question["id"],
                    question=question["question"],
                    answers=question["answers"]) for question in data]
