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
  statistics = {}
