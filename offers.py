from inventory import Inventory
from product import ProductEnum
from discount import Discount

class OfferManagement:
# it will help in choosing conditions of what type of offers admin want to create

    @staticmethod
    def update_category_offer(inventory, category, discount_percentage):
        products = inventory.get_product_by_category(category)
        for product in products:
            if product["id"] in inventory.discounts:
                discount = inventory.discounts[product.id]
                discount.discount = discount_percentage
            else:
                Discount(product["id"], discount_percentage, inventory)
        
    
    @staticmethod
    def update_discount_details(inventory, productId, quantity, discount_percentage):
        discount = inventory.discounts[productId]
        discount.update_discount_details(quantity, discount_percentage)

    
    


    
    


    

    



    
    