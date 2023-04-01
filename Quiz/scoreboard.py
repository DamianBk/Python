class Scoreboard:

    def __init__(self, *args):
        self.__score_data = [args]

    @property
    def player(self):
        return self.__score_data
    
    @player.setter
    def player(self, *args):
        self.__score_data.append(args)
        
    @player.deleter
    def player(self):
        return self.__score_data.clear()

    def save_score(self):
        with open("scoreboard.txt", "a+", encoding="utf-8") as file_write:
            for player in self.__score_data:
                for info in player:
                    file_write.write(f"{info[0]}, {info[1]}")
                    file_write.write("\n")
                    
    @property
    def show_message(self):
        for player in self.__score_data:
            for info in player:
                print(f"Gratuluję {info[0]}, łączna ilość uzyskanych punktów: {info[1]}, ilość popełnionych błędów: {info[2]}")
