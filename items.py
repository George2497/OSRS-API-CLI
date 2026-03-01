from OSRSBytes import Items

item = None

class ItemSearch:

  def __init__(self, item):
    self.item = Items(item)

  def find_item(self, item_name):

    print("Is Members: ", self.item.isMembers(item_name))
    print("Item ID: ", self.item.getItemID(item_name))

    print("Sell Average: ", self.item.getSellAverage(item_name), "gp")
    print("Sell Quantity: ", self.item.getSellQuantity(item_name))

    print("Buy Average ", self.item.getBuyAverage(item_name), "gp")
    print("Buy Quantity: ", self.item.getBuyQuantity(item_name))
    print("Buy Limit: ", self.item.getBuyLimit(item_name))

    print("Shop Price ", self.item.getShopPrice(item_name), "gp")
    print("High Alch Value: ", self.item.getHighAlchValue(item_name), "gp")
    print("Low Alch Value: ", self.item.getLowAlchValue(item_name), "gp")

