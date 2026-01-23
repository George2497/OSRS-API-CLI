from OSRSBytes import Hiscores
import highscores
import items
import bosses
import cluescrolls

class searchInformation:
  def search(self):
    pass

def main():
  hs = highscores.Highscore()
  hs.findPlayer()

  it = items.ItemSearch()
  it.findItem()

  cs = cluescrolls.ClueScroll()
  cs.findClueScroll()

  osrsSearch = searchInformation()
  osrsSearch.search()

if __name__=="__main__":
  main()