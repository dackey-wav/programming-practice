class TennisGame3:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def is_normal_score(self):
        return (
            self.player1_score < 4
            and self.player2_score < 4
            and not (self.player1_score == 3 and self.player2_score == 3)
        )

    def score(self):
        if self.is_normal_score():
            player1_score_name = self.SCORE_NAMES[self.player1_score]
            if self.player1_score == self.player2_score:
                return player1_score_name + "-All"
            return player1_score_name + "-" + self.SCORE_NAMES[self.player2_score]

        if self.player1_score == self.player2_score:
            return "Deuce"

        leading_player_name = (
            self.player1_name
            if self.player1_score > self.player2_score
            else self.player2_name
        )
        if abs(self.player1_score - self.player2_score) == 1:
            return "Advantage " + leading_player_name
        return "Win for " + leading_player_name
