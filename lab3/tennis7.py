class TennisGame7:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def score_name(self, score):
        return self.SCORE_NAMES[score]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1
        else:
            raise ValueError("Invalid player name.")

    def _tied_score(self):
        if self.player1_score < 3:
            return self.score_name(self.player1_score) + "-All"
        return "Deuce"

    def _endgame_score(self):
        score_diff = self.player1_score - self.player2_score
        if score_diff == 1:
            return "Advantage " + self.player1_name
        if score_diff == -1:
            return "Advantage " + self.player2_name
        if score_diff >= 2:
            return "Win for " + self.player1_name
        return "Win for " + self.player2_name

    def _regular_score(self):
        return self.score_name(self.player1_score) + "-" + self.score_name(self.player2_score)

    def score(self):
        if self.player1_score == self.player2_score:
            result = self._tied_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            result = self._endgame_score()
        else:
            result = self._regular_score()

        return "Current score: " + result + ", enjoy your game!"