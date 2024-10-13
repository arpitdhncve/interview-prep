class Discount:

    def __init__(self, productid, discount, inventory):
        self.productId = productid
        self.discount = discount
        self.quantity = 1
        inventory.discounts[productid] = self
    
    def update_discount_details(self, quantity, discount):
        self.quantity = quantity
        self.discount = discount
        return True

    

    

    

    
    
