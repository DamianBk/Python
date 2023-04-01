class Highestscore:
    
    def __init__(self, score_file):
        self.__score_file = score_file
    
    def get_highest_scores(self):
        scoreboard = {}
        with open(self.__score_file, "r", encoding="utf-8") as file_score:
            scores = file_score.readlines()
            sorted_score = sorted(
                scores, key=lambda x: x.split(",")[1], reverse=True)
        for index, users in enumerate(sorted_score, 1):
            name = users.replace("\n", "").split(",")[0]
            score = users.replace("\n", "").split(",")[1]
            scoreboard[index] = [name, score]
            
        return scoreboard
    
    @property
    def show_high_score(self):
        score = self.get_highest_scores()
        for index , player in score.items():
            print(f"Miejsce {index}: Imię: {player[0].capitalize()}, Punkty: {player[1]}")
