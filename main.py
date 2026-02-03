from OSRSBytes import Hiscores
import highscores
from highscores import normalize_skill
import items
import bosses
import cluescrolls

class searchInformation:
  def menu(self):
    print("If you would like to quit, press ENTER")
    print("What would you like to look up?:\n" \
    "1. Stats\n" \
    "2. Item\n" \
    "3. Clue Scrolls\n" \
    "4. Bosses")

    choice = input("> ").strip()

    if choice == "1":
      self.stats_lookup()
    elif choice == "2":
      self.item_lookup()
    elif choice == "3":
      self.clue_lookup()
    elif choice == "4":
      self.boss_lookup()
    elif choice == "5":
      self.all_skills()
    else:
      print("Invalid value")

  def stats_lookup(self):
    username = input("Enter username: ")
    if username == "":
      print("Thank you for using OSRS CLI...goodbye")
      quit()

    skillname = input("Which skill would you like to view?: ").strip().lower()
    if skillname == "":
      print("Thank you for using OSRS CLI...goodbye")
      quit()

    skillname = normalize_skill(skillname)
    hs = highscores.Highscore(username)
    hs.show_skill(skillname)
    searchInformation.menu(self)
  
  def item_lookup(self):
    item = input("Enter item: ").strip().lower()
    if item == "":
      print("Thank you for using OSRS CLI...goodbye")
      quit()

    it = items.ItemSearch(item)
    it.find_item(item)
    searchInformation.menu(self)

  def clue_lookup(self):
    username = input("Enter username: ").strip().lower()
    if username == "":
      print("Thank you for using OSRS CLI...goodbye")
      quit()

    clues = input("Which clue scrolls would you like to look up? \n" \
    "beginner, easy, medium, hard, elite, master: ")
    if clues == "":
      print("Thank you for using OSRS CLI...goodbye")
      quit()

    cs = cluescrolls.ClueScroll(username)
    cs.find_clue_scroll(clues)
    searchInformation.menu(self)

  def boss_lookup(self):
    username = input("Enter username: ")
    if username == "":
      print("Thank you for using OSRS CLI...goodbye")
      quit()

    bossname = input("Which boss would you like to look up?: ")
    if bossname == "":
      print("Thank you for using OSRS CLI...goodbye")
      quit()
    hs = bosses.Bosses(username)
    hs.find_boss(bossname)

def main():
  osrsSearch = searchInformation()
  osrsSearch.menu()

if __name__=="__main__":
  main()