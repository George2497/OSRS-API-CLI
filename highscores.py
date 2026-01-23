from OSRSBytes import Hiscores

class Highscore:
  def findPlayer():
    user = Hiscores("EliteGk 24")

# can set skill name to variable and assign from input to find any skill typed in
# Skills
    print("Current level: ", user.skill("attack", "level"))
    print("Current rank: ", user.skill("attack", "rank"))
    print("Current exp: ", user.skill("attack", "experience"))
    print("Exp remaining: ", user.skill("attack", "exp_to_next_level"))

# Bosses
    print("Wintertodt Kills: ", user.boss("wintertodt", "score"))

# Medium clues
    print("Medium clues done: ", user.clue("medium", "score"))

def main():
  HS = Highscore
  HS.findPlayer()

if __name__=="__main__":
  main()