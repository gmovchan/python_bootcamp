from IPython.display import clear_output
import csv

class ShoppingCart():
    def __init__(self):
        self.cart = self.loadCart()
        
    def addItem(self, item):
        clear_output()
        self.cart.append(item)
        print("{} has been added.".format(item))
    
    
    def removeItem(self, num):
        clear_output()
        try:
            indexItem = int(num) - 1
            item = self.cart[indexItem]
            self.cart.pop(indexItem)
            print("{}) {} has been removed.".format(num, item))
        except:
            print("Sorry we could not remove that item.")


    def showCart(self):
        clear_output()
        if self.cart:
            print("Here is your cart:")
            i = 1
            for item in self.cart:
                print("{}) {}".format(i, item))
                i += 1
        else:
            print("Your cart is empty.")


    def clearCart(self):
        clear_output()
        self.cart.clear()
        print("Your cart is empty.")


    def main(self):
        done = False

        while not done:
            ans = input("quit/add/remove/show/clear: ".lower())

            if ans == "quit":
                print("Thanks for using our program.")
                self.showCart()
                self.saveCart()
                done = True
            elif ans == "add":
                item = input("What would you like to add? ").title()
                self.addItem(item)
            elif ans == "remove":
                self.showCart()
                num = input("What would you like to remove? Type the item number ").title()
                self.removeItem(num)
            elif ans == "show":
                self.showCart()
            elif ans == "clear":
                self.clearCart()
            else:
                print("Sorry that was not an option.")
    
    def loadCart(self):
      with open("cart.csv", mode = "r") as f:
        reader = csv.reader(f, delimiter = ",")
        cart = list(reader)
        return cart[0]
      
    
    def saveCart(self):
      with open("cart.csv", mode = "w", newline = "") as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerows([self.cart])
      