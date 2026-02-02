from OSRSBytes import Hiscores

clue = None

class ClueScroll:
  def __init__(self, username):
    self.username = username
    self.user = Hiscores(username)

  def find_clue_scroll(self, cluescroll_type):
    option = {
      "beginner" : lambda: print("Beginner clues done: ", self.user.clue("beginner", "score")),
      "easy" : lambda: print("Easy clues done: ", self.user.clue("easy", "score")),
      "medium" : lambda: print("Medium clues done: ", self.user.clue("medium", "score")),
      "hard" : lambda: print("Hard clues done: ", self.user.clue("hard", "score")),
      "elite" : lambda: print("Elite clues done: ", self.user.clue("elite", "score")),
      "master" : lambda: print("Master clues done: ", self.user.clue("master", "score")),
    }

    if cluescroll_type in option :
      option[cluescroll_type]()
    else:
      print("Please enter a valid option...")