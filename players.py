# This will be the code to generate, save, and recall players

# define  the Player class
class Player:
  def __init__(self,name):
    self.name = name

  def __str__(self):
    return f"{self.name}"

  # Player Characteristics
  animal = 'none'
  height = 0
  weight = 0
  handedness = 'none'
  topSpeed = 0
  acceleration = 0
  strength = 0

  # Stats - Dictionary (maybe should be list?) that is added to after every game
  statistics = dict(hits=0,
                    walks=0,
                    strikeouts=0,
                    hit_by_pitch=0,
                    runs=0,
                    rbis=0,
                    singles=0,
                    doubles=0,
                    triples=0,
                    home_runs=0)
