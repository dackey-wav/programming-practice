class TennisGame5:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        # if player_name == "player1":                            # hardcoded name
        if player_name == self.player1_name:    
            self.player1_score += 1
        # elif player_name == "player2":                          # hardcoded name
        elif player_name == self.player2_name:    
            self.player2_score += 1
        else:
            raise ValueError("Invalid player name.")

    def score(self):
        player1_score = self.player1_score
        player2_score = self.player2_score

        if player1_score < 4 and player2_score < 4:
            if player1_score == player2_score:
                if player1_score == 3:
                    return "Deuce"
                return f"{self.SCORE_NAMES[player1_score]}-All"
            return f"{self.SCORE_NAMES[player1_score]}-{self.SCORE_NAMES[player2_score]}"
        
        if player1_score == player2_score:
            return "Deuce"

        leader = self.player1_name if self.player1_score > self.player2_score else self.player2_name

        if abs(player1_score - player2_score) == 1:
            return f"Advantage {leader}"
        return f"Win for {leader}"
