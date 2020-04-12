
#Ben Bennington
"""
Put your code here.
"""
        
#This creates a class for the product and its properties
class Product:
    def __init__(self, id, name, price, quantity):
        self.name = name
        self.id = id
        self.price = price
        self.quantity = quantity
        
#This will find the total price        
    def get_total_price(self):
        return self.price * self.quantity
        
        
#This will display the price    
    def display(self):
        print('{}({}) - ${:.2f}'.format(self.name,self.quantity,self.get_total_price()))


#This creates a class for the Order and its properties
class Order:
    def __init__(self):
        self.id = id
        self.products = []
        
#This will find your subtotal        
    def get_subtotal(self):
        summ = 0
        for i in self.products:
            summ += i.get_total_price()
        return summ
#This will calulate the tax sum for you    
    def get_tax(self):
        return self.get_subtotal()*0.065
#This will add the subtotal and the tax     
    def get_total(self):
        return self.get_tax()+self.get_subtotal()
#This will append the products    
    def add_product(self, product):
        self.products.append(product)
#This will display the reciept of the order    
    def display_receipt(self):
        print('Order: {}'.format(self.id))
        for product in self.products:
            product.display()
            
        print('Subtotal: ${:.2f}'.format(self.get_subtotal()))
        print('Tax: ${:.2f}'.format(self.get_tax()))
        print('Total: ${:.2f}'.format(self.get_total()))

#This creates a class for the Customer and its properties
class Customer:
    def __init__(self):
        self.name = ''
        self.orders = []
        self.id = ''
#This is counting the orders        
    def get_order_count(self):
        return len(self.orders)
#This will find the total     
    def get_total(self):
        newSum = 0
        for i in self.orders:
            newSum += i.get_total()
        return newSum
#This will append the order    
    def add_order(self, order):
        self.orders.append(order)
#This will display a summary of the orders    
    def display_summary(self):
        print("Summary for customer '{}':".format(self.id))
        print('Name: {}'.format(self.name))
        print('Orders: {}'.format(self.get_order_count()))
        print('Total: ${:.2f}'.format(self.get_total()))
#This is a display of the reciept    
    def display_receipts(self):
        for i in self.orders:
            i.display_receipt()
        
 
    
    
    
    
    
    

def main():
    """ Do Not Change This Function """
    
    print("### Testing Products ###")
    p1 = Product("1238223", "Sword", 1899.99, 10)

    print("Id: {}".format(p1.id))
    print("Name: {}".format(p1.name))
    print("Price: {}".format(p1.price))
    print("Quantity: {}".format(p1.quantity))

    p1.display()

    print()

    p2 = Product("838ab883", "Shield", 989.75, 6)
    print("Id: {}".format(p2.id))
    print("Name: {}".format(p2.name))
    print("Price: {}".format(p2.price))
    print("Quantity: {}".format(p2.quantity))

    p2.display()

    print("\n### Testing Orders ###")
    # Now test Orders
    order1 = Order()
    order1.id = "1138"
    order1.add_product(p1)
    order1.add_product(p2)

    order1.display_receipt()

    print("\n### Testing Customers ###")
    # Now test customers
    c = Customer()
    c.id = "aa32"
    c.name = "Gandalf"
    c.add_order(order1)

    c.display_summary()

    print()
    c.display_receipts()

    # Add another product and order and display again

    p3 = Product("2387127", "The Ring", 1000000, 1)
    p4 = Product("1828191", "Wizard Staff", 199.99, 3)

    order2 = Order()
    order2.id = "1277182"
    order2.add_product(p3)
    order2.add_product(p4)

    c.add_order(order2)

    print()
    c.display_summary()

    print()
    c.display_receipts()


if __name__ == "__main__":
    main()