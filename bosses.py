from OSRSBytes import Hiscores
import highscores

class Bosses:
  def findBoss():
    boss = input("Please enter a boss: ")
    bossname = boss
    # Bosses
    print("Wintertodt Kills: ", highscores.user.boss(bossname, "score"))

def main():
  HS = Bosses
  HS.findBoss()

if __name__=="__main__":
  main()