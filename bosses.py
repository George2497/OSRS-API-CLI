from OSRSBytes import Hiscores
from rapidfuzz import process, fuzz

bossname = None

boss_names = [
    "abyssal_sire", "alchemical_hydra", "barrows_chests", "bryophyta",
    "callisto", "cerberus", "chambers_of_xeric", "chambers_of_xeric_challenge_mode",
    "chaos_elemental", "chaos_fanatic", "commander_zilyana", "corporeal_beast",
    "crazy_archaeologist", "dagannoth_prime", "dagannoth_rex", "dagannoth_supreme",
    "deranged_archaeologist", "gauntlet", "gauntlet_corrupted",
    "giant_mole", "grotesque_guardians", "hespori",
    "kalphite_queen", "king_black_dragon", "kraken", "kreearra",
    "kril_tsutsaroth", "mimic", "nightmare", "phosanis_nightmare",
    "obor", "sarachnis", "scorpia", "skotizo",
    "tempoross", "the_whisperer", "tzkal_zuk", "videssence",
    "vorkath", "wintertodt", "zalcano", "zulrah"
    ]

def find_valid_boss(user_input):
    user_input = user_input.lower()
    if user_input in boss_names:
      return user_input
    
    match, score, _ = process.extractOne(user_input, boss_names, scorer=fuzz.ratio)

    if score >= 80:
      return match
    else:
      return None

class Bosses:
  def __init__(self, username):
    self.username = username
    self.user = Hiscores(username)
    self.bosses = boss_names
    
  def find_boss(self, bossname):
    print(f"{self.username}'s information for {bossname}")

    if bossname not in self.bosses:
      print("Boss not found...")
      return
    
    count = self.user.boss(bossname)
    print(f"{bossname.replace('_', ' ').title()}: {count}")