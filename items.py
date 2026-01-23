from OSRSBytes import Items

item = None

class ItemSearch:
  def findItem(self):
    global item
    items = input("Enter an item: ")
    item = Items(items)

    print("Is Members: ", item.isMembers(items))
    print("Item ID: ", item.getItemID(items))

    print("Sell Average: ", item.getSellAverage(items), "gp")
    print("Sell Quantity: ", item.getSellQuantity(items))

    print("Buy Average ", item.getBuyAverage(items), "gp")
    print("Buy Quantity: ", item.getBuyQuantity(items))
    print("Buy Limit: ", item.getBuyLimit(items))

    print("Shop Price ", item.getShopPrice(items), "gp")
    print("High Alch Value: ", item.getHighAlchValue(items), "gp")
    print("Low Alch Value: ", item.getLowAlchValue(items), "gp")

    print("Item Name: ", item.getName(items))
    print("Sell Average: ", item.getSellAverage(items), "gp")

    item.update()

    print("Sell Average: ", item.getSellAverage(items), "gp")

def main():
  itLookup = ItemSearch()
  itLookup.findItem()

if __name__=="__main__":
  main()
