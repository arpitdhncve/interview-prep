from discount import Discount
from productView import WithoutDiscount


class Inventory:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Inventory, cls).__new__(cls)
            cls.products = []
            cls.discounts = {}
            cls.product_view_strategy = WithoutDiscount()
            return cls._instance
        

    def get_all_products(self):
        products = self.product_view_strategy.get_list(self, None)
        return products

    
    def get_product_by_category(self, category):
        products = self.product_view_strategy.get_list(self, category)
        return products
    


    def update_discount_status(self, product_view_startegy):
        self.product_view_strategy = product_view_startegy



    

    

    
