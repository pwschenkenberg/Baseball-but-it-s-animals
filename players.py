# This will be the code to generate, save, and recall players

# define  the Player class
class Player:
  def __init__(self,name):
    self.name = name

  def __str__(self):
    return f"{self.name}"
