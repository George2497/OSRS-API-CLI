from OSRSBytes import Hiscores
import highscores

clue = None

class ClueScroll:
  def findClueScroll(self):
    cluescrolls = input("Which clue scrolls would you like to look up? \n" \
    "beginner, easy, medium, hard, elite, master: ")
    clue = Hiscores(cluescrolls)

    if cluescrolls.lower() == 'beginner':
      print("Beginner clues done: ", highscores.user.clue(cluescrolls, "score"))

    if cluescrolls.lower() == 'easy':
      print("Easy clues done: ", highscores.user.clue(cluescrolls, "score"))

    if cluescrolls.lower() == 'medium':
      print("Medium clues done: ", highscores.user.clue(cluescrolls, "score"))

    if cluescrolls.lower() == 'hard':
      print("Hard clues done: ", highscores.user.clue(cluescrolls, "score"))

    if cluescrolls.lower() == 'elite':
      print("Elite clues done: ", highscores.user.clue(cluescrolls, "score"))

    if cluescrolls.lower() == 'master':
      print("Master clues done: ", highscores.user.clue(cluescrolls, "score"))


def main():
  cslLookup = ClueScroll()
  cslLookup.findClueScroll()

if __name__=="__main__":
  main()