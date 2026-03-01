from OSRSBytes import Hiscores
from rapidfuzz import process, fuzz

clue = None

class ClueScroll:
  def __init__(self, username):
    self.username = username
    self.user = Hiscores(username)
    self.option = {
      "beginner" : lambda: print("Beginner clues done: ", self.user.clue("beginner", "score")),
      "easy" : lambda: print("Easy clues done: ", self.user.clue("easy", "score")),
      "medium" : lambda: print("Medium clues done: ", self.user.clue("medium", "score")),
      "hard" : lambda: print("Hard clues done: ", self.user.clue("hard", "score")),
      "elite" : lambda: print("Elite clues done: ", self.user.clue("elite", "score")),
      "master" : lambda: print("Master clues done: ", self.user.clue("master", "score")),
    }

  def find_valid_clue(self, user_input):
    user_input = user_input.lower()
    if user_input in self.option:
      return user_input
    
    match, score, _ = process.extractOne(user_input, self.option.keys(), scorer=fuzz.ratio)

    if score >= 80:
      return match
    else:
      return None
    
  def find_clue_scroll(self, cluescroll_type):
    if cluescroll_type in self.option :
      self.option[cluescroll_type]()
    else:
      print("Please enter a valid option...")
