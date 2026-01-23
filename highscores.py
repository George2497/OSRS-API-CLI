from OSRSBytes import Hiscores

user = None

class Highscore:
  def findPlayer(self):
    # Searches for a player and loads their profile
    global user
    target_username = input("Enter a username: ")
    user = Hiscores(target_username) 

    # Skills
    trainingMethod = input("Which skill would you like to view?: ").lower()
    print("Current level: ", user.skill(trainingMethod, "level"))
    print("Current rank: ", user.skill(trainingMethod, "rank"))
    print("Current exp: ", user.skill(trainingMethod, "experience"))
    print("Exp remaining: ", user.skill(trainingMethod, "exp_to_next_level"))


def main():
  hslookup = Highscore()
  hslookup.findPlayer()

if __name__=="__main__":
  main()