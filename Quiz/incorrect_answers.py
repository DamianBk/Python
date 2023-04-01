class IncorrectAnswers:
    def __init__(self):
        self.__list_answers = []
    
    @property
    def add_answer(self):
        return self.__list_answers
    
    @add_answer.setter
    def add_answer(self, *args):
        self.__list_answers.append(*args)
        
    @add_answer.deleter
    def add_answer(self):
        self.__list_answers.clear()
    
    @property
    def messages_incorrect(self):
        message = f"Popełniłeś błędy w następujących pytaniach:\n"
        for question in self.add_answer:
            message += f"Pytanie {question[0]}: {question[1][:-1]}\n"
        return message
    