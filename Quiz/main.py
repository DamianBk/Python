import json
from questions import Questions, LoadQuestions
from scoreboard import Scoreboard
from highestscore import Highestscore
from player import Player


class Quiz:

    def __init__(self, path_file: str):
        self.path_file = path_file
        self.player = Player("scoreboard.txt")
        self.high_score = Highestscore("scoreboard.txt")
        self.questions = LoadQuestions("questions.json")

    def run_quiz(self):
        while True:
            self.player.player(input("Podaj swoje imię: "))
            questions = self.questions._load_questions()  #type:ignore
            for question in questions:  # type:ignore
                question.show_question
                self.__check_answer(question)
            self.__save_score()
            self.__show_incorrect_answers()

            if not self.__is_continue():
                self.__show_high_scores()
                break
    
    def __check_answer(self, question: Questions):
        while True:
            answer = input("Wybierz odpowiedź: ").upper()
            print()
            if self.__is_correct_key(answer, question._answers.keys()):  # type:ignore
                self.__is_correct_answer(answer, question)
                break
            else:
                print("Opcje wyboru: A B C lub D")
    # checking the answer.
    def __is_correct_answer(self, user_answer: str, question: Questions):
        if question._is_correct(user_answer):  #type:ignore
            self.player.correct_score()
        else:
            self.player.incorrect_score()
            self.player.incorrect_answers(
                question._id_question, question._question)
    # checking if the selected option is available.
    def __is_correct_key(self, user_answer: str, keys) -> bool:
        if user_answer in keys:
            return True
        else:
            print("Podałeś niedostępną opcję wyboru, spróbuj ponownie.")
            return False
    
    def __is_continue(self) -> bool:
        while True:
            answer = input("\nChcesz grać dalej T/N ?: ").upper()
            if self.__is_correct_key(answer, ["T", "N"]):
                match answer:
                    case "T":
                        self.player.incorrect_answers_clear()
                        self.player._name = ""
                        self.player._correct_score = 0
                        self.player._incorrect_score = 0
                        return True
                    case "N":
                        return False
                    case _:
                        pass
            else:
                print("Wprowadź poprawną literę aby zakończyć/kontynuować quiz")

    def __save_score(self):
        self.player.show_message
        self.player.save_score()

    def __show_incorrect_answers(self) -> None:
        if self.player._incorrect_score > 0:
            self.player.show_message_inccorect

    def __show_high_scores(self):
        self.high_score.get_highest_scores()
        self.high_score.show_high_score


if __name__ == "__main__":
    quiz = Quiz("questions.json")
    quiz.run_quiz()
