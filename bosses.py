from OSRSBytes import Hiscores
import highscores

bossname = None

class Bosses:
  def __init__(self, username):
    self.username = username
    self.user = Hiscores(username)
    self.bosses = [
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

  def find_boss(self, bossname):
    bossname = bossname.strip().lower()

    if bossname not in self.bosses:
      print("Boss not found...")
      return
    
    count = self.user.boss(bossname)
    print(f"{bossname.replace('_', ' ').title()}: {count}")