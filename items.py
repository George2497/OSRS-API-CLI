from OSRSBytes import Items

class Item:
  def findItem():
    items = Items()
    print("Is Members: ", items.isMembers('rune dagger'))
    print("Item ID: ", items.getItemID('rune dagger'))

    print("Sell Average: ", items.getSellAverage('rune dagger'), "gp")
    print("Sell Quantity: ", items.getSellQuantity('rune dagger'))

    print("Buy Average ", items.getBuyAverage('rune dagger'), "gp")
    print("Buy Quantity: ", items.getBuyQuantity('rune dagger'))
    print("Buy Limit: ", items.getBuyLimit('rune dagger'))

    print("Shop Price ", items.getShopPrice('rune dagger'), "gp")
    print("High Alch Value: ", items.getHighAlchValue('rune dagger'), "gp")
    print("Low Alch Value: ", items.getLowAlchValue('rune dagger'), "gp")

    print("Item Name: ", items.getName('rune dagger'))
    print("Sell Average: ", items.getSellAverage('rune dagger'), "gp")

    items.update()

    print("Sell Average: ", items.getSellAverage('rune dagger'), "gp")

def main():
  HS = Item
  HS.findItem()

if __name__=="__main__":
  main()
