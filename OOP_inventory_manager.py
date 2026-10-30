class Product:
 
    # __init__ runs automatically when a new Product is created
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)   # price is a decimal number
        self.__stock = int(stock)     # stock is a whole number
 
    # Getter: return the product ID
    def get_product_id(self):
        return self.__product_id
 
    # Getter: return the product name
    def get_name(self):
        return self.__name
 
    # Getter: return the price
    def get_price(self):
        return self.__price
 
    # Getter: return the stock amount
    def get_stock(self):
        return self.__stock
 
    # Change the stock - the Product checks the value first (encapsulation)
    def update_stock(self, quantity):
        if quantity < 0:
            print("Stock cannot be negative. No change made.")
            return False   # update failed
        self.__stock = quantity
        return True        # update worked
 
    # Print this product's details on one line
    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")
 
 
# =====================================================================
# Temporary test for Chunk 1 (we will replace this with the menu later)
# =====================================================================
if __name__ == "__main__":
    test_product = Product("P001", "Laptop", 1200.00, 15)   # create a product
    test_product.display_information()                      # shows stock 15
    test_product.update_stock(20)                           # change stock to 20
    test_product.display_information()                      # shows stock 20
    test_product.update_stock(-5)                           # should be refused
 