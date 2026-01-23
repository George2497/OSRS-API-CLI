from OSRSBytes import Hiscores
import highscores

bossname = None

class Bosses:
  def findBoss(self):
    boss = input("Please enter a boss: ")
    bossname = boss
    # Bosses
    print(bossname, " Kills: ", highscores.user.boss(bossname, "score"))

def main():
  bossLookup = Bosses
  bossLookup.findBoss()

if __name__=="__main__":
  main()