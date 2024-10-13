from product import Clothing, Electronics, Food, ProductEnum

class Productfactory:
    
    @staticmethod
    def create_product(product_type : ProductEnum, product_details, inventory):
        if product_type == ProductEnum.CLOTHING:
            return Clothing(product_details, inventory)
        elif product_type == ProductEnum.ELECTRONICS:
            return Electronics(product_details, inventory)
        elif product_type == ProductEnum.FOOD:
            return Food(product_details, inventory)
        else:
            return ("Unknown category")






    