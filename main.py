"""
Word Football
"""
import datetime
from csv_read import open_csv
from text import open_text

def choose_language():
    """
    Choosing language
    """
    while True:
        language = input("Pick language - cs/en: ")
        if language in ("cs", "en"):
            return language

class WordFootball:
    """
    Word Football
    """
    def __init__(self):
        self._started = True
        self._used_words = []
        self._player_two = ""
        self.texts = texts
        self.words_csv = words_csv

    def check_second_player(self, player_one):
        """
        Second Player
        """
        while True:
            self._player_two= input(texts[choosed_language]["sentence2"])
            if self._player_two in words_csv:
                continue
            for row in words_csv:
                word = row[0]
                if self._player_two == word and self._player_two not in self._used_words:
                    self._used_words.append(self._player_two)
                    if self._player_two[0] == player_one[-1]:
                        return

    def check_first_player(self):
        """
        First Player
        """
        while True:
            player_one = input(texts[choosed_language]["sentence1"])
            if player_one in words_csv:
                continue
            for row in words_csv:
                word = row[0]
                if player_one == word and player_one not in self._used_words:
                    if self._started:
                        self._used_words.append(player_one)
                        self._started = False
                        self.check_second_player(player_one)
                        break
                    if self._player_two[-1] == player_one[0]:
                        self.check_second_player(player_one)
                        break

if __name__ == "__main__":
    current_time = datetime.datetime.now()
    current_time = current_time.strftime("%H:%M:%S")
    choosed_language = choose_language()
    texts = open_text()
    words_csv = open_csv()
    print(texts[choosed_language]["date"], current_time)
    call = WordFootball()

    while True:
        call.check_first_player()
