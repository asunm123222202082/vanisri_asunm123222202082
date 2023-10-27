# define the base class player
class Player:
  def play(self):
    print("The player is playing cricket.")
# Define the derived class Batsma
class Batsman(Player):
  def play(self):
    print("The batsman is batting.")
# Define the derived class Bowler 
class Bowler(Player):
  def play(self):
    print("The bowler is bowling.")
# Create objects of Batsman and Bouter classes
batsman = Batsman()
bowler = Bowler()
#call the play() method for each object
batsman.play()
bowler.play()