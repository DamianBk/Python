class Player:
    def __init__(self, score_file):
        self._name = ""
        self._correct_score = 0
        self._incorrect_score = 0
        self.__score_file = ""
        self.__incorrect_answers = []
        self.__score_file = score_file
    
    def player(self, name):
        self._name = name

    def correct_score(self):
        self._correct_score += 1

    def incorrect_score(self):
        self._incorrect_score += 1

    def save_score(self):
        with open(self.__score_file, "a+", encoding="utf-8") as file_write:
            file_write.write(f"{self._name}, {self._correct_score}")
            file_write.write("\n")

    def incorrect_answers(self, *args):
        self.__incorrect_answers.append(args)

    def incorrect_answers_clear(self):
        self.__incorrect_answers.clear()

    @property
    def show_message_inccorect(self):
        message = f"Popełniłeś błędy w następujących pytaniach:\n"
        questions = [q for q in self.__incorrect_answers]
        for question in questions:
            message += f"Pytanie {question[0]}: {question[1][:-1]}\n"
        print(message)

    @property
    def show_message(self):
        print(
            f"Gratuluję {self._name}, łączna ilość uzyskanych punktów: {self._correct_score}, ilość popełnionych błędów: {self._incorrect_score}")
