
class ScoreCard:

    def __init__(self, score_card):
        
        self.string = score_card
        self.rolls = self.parse_rolls()

    def get_rolls(self):
          return self.rolls

    def _parse_rolls(self):

        rolls=[]
        for char in self.string:
            if char == "X":
                    rolls.append(10)

            elif char == "/":
                    rolls.append(10 - rolls [-1])

            elif char == "-":
                    rolls.append(0)

            else:
                    rolls.append(int(char))

        return rolls
        

    def score(self):
        total = 0
        frame= 0

        for _ in range(10):
            if self.is_strike(frame):
                  total += 10 + self._strike_bonus(frame)
                  frame += 1
            elif self.is_spare(frame):
                  total += 10 + self._strike_bonus(frame)
                  frame += 2
            else:
                  first = self.rolls[frame]
                  second = self.roles [frame + 1] if frame + 1 < len(self.rolls) else 0
                  total = first + second
                  frame += 2
        return total
                  