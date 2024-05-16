# this will be the code to create, store, and manage games

# Create Game class
class Game:
  def __init__(self,home_team,away_team):
    self.home_team = home_team
    self.away_team = away_team

  def __str__(self):
    return f"{self.home_team} vs {self.away_team}"
  
