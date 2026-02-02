from OSRSBytes import Hiscores

user = None

class Highscore:
  def __init__(self, username):
    self.username = username
    self.user = Hiscores(username)

  def show_skill(self, skill):

    # Skills
    print(f"\nHere is the {skill} skill information for {self.username}\n")
    print("Current level: ", self.user.skill(skill, "level"))
    print("Current rank: ", self.user.skill(skill, "rank"))
    print("Current exp: ", self.user.skill(skill, "experience"))
    print("Exp remaining: ", self.user.skill(skill, "exp_to_next_level"))


  def show_all_skills(self):
    skillsList = [
      "attack", "strength", "defence", "ranged", "prayer",
      "magic", "hitpoints", "runecrafting", "crafting", "mining",
      "smithing", "fishing", "cooking", "firemaking", "woodcutting",
      "agility", "herblore", "thieving", "fletching", "slayer",
      "farming", "construction", "hunter"
    ]

    for skill in skillsList:
      self.show_skill(skill)

def normalize_skill(skill):
  aliases = {
    "atk" : "attack",
    "str" : "strength",
    "defence" : "defense",
    "def" : "defense",
    "rng" : "ranged",
    "pray" : "prayer",
    "mgk" : "magic",
    "hit points" : "hitpoints",
    "hp" : "hitpoints",
    "rc" : "runecrafting",
    "craft" : "crafting",
    "mine" : "mining",
    "smith" : "smithing",
    "fish" : "fishing",
    "cook" : "cooking",
    "fire" : "firemaking",
    "fm" : "firemaking",
    "wood" : "woodcutting",
    "wc" : "woodcutting",
    "agil" : "agility",
    "herb" : "herblore",
    "hb" : "herblore",
    "thiev" : "thieving",
    "fletch" : "fletching",
    "slay" : "slayer",
    "farm" : "farming",
    "const" : "construction",
    "hunt" : "hunter"
  }
  return aliases.get(skill, skill)