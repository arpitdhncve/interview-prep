from os import stat
from product import ProductEnum
from productFactory import Productfactory
from inventory import Inventory


class InventoryManagement:

    @staticmethod
    def add_product(inventory: Inventory, product_details, productType: ProductEnum):
        product = Productfactory.create_product(productType, product_details, inventory)
        inventory.products.append(product)
    
    @staticmethod
    def update_quantity(inventory: Inventory, productId, quantity, is_purchased):
        product = None
        for product in inventory.products:
            if productId == product.id:
                product = product
        if is_purchased:
            product.stock -= quantity
        else:
            product.stock += quantity





            

